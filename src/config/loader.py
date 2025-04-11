import os
import toml

env = os.getenv("ENV", "dev")

config_file = f"config/config.{env}.toml"

# Load the configuration file
with open(config_file, "r") as f:
    config = toml.load(f)