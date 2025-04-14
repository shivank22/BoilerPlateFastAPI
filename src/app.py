import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from config.loader import config
import routes
import importlib
import pkgutil
from routes.error import http_exception_handler, validation_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logger.info("Starting FastAPI application...")

app = FastAPI(
    title="FastAPI App with Azure Managed Identity",
    description="This API demonstrates modular routing, Pydantic validation, Azure authentication, Postgres integration, and auto-generated OpenAPI docs.",
    version="1.0.0",
)

ENV = os.getenv("ENV", "development")

if ENV == "production":
    allowed_origins = ["https://your-frontend.com"]  # <- Replace with your actual frontend
else:
    allowed_origins = ["*"]  # Allow all in development

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],
)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

for _, module_name, _ in pkgutil.iter_modules(routes.__path__):
    module = importlib.import_module(f"routes.{module_name}")
    if hasattr(module, "router"):
        app.include_router(module.router, dependencies=[Depends(lambda: config)])

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}