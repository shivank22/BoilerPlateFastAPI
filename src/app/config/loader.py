import os
import toml

env = os.getenv("ENV", "dev")

base_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(base_dir, f"config.{env}.toml")

with open(config_file, "r") as f:
    config = toml.load(f)