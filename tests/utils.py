import json
from pathlib import Path

ROOT = Path(__file__).parent


def loads(path):
    with open(path) as f:
        return json.loads(f.read())


def text(path):
    with open(path) as f:
        return f.read()
