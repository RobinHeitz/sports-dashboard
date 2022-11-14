import toml
from pathlib import Path

p = Path("config.toml")

with open(p) as f:
    config = toml.load(f)


print("TOML Config = ", config)
