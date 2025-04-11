# Project Structure
app/
├── app.py
├── config/
│   ├── config.toml
│   └── loader.py
├── docs/
│   ├── __init__.py
│   ├── users_docs.py
│   ├── tasks_docs.py
│   └── models_docs.py
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── user.py
│   └── task.py
├── db/
│   ├── __init__.py
│   ├── session.py
│   └── migrations/  ← (Alembic directory)
├── routes/
│   ├── __init__.py
│   ├── users.py
│   └── tasks.py
├── auth/
│   └── azure_auth.py
├── tests/
│   ├── __init__.py
│   └── test_users.py
└── Dockerfile

find . -type d -name "__pycache__" -exec rm -rf {} +
