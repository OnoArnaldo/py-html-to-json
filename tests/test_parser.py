import json
from pathlib import Path

import html_to_json

ROOT = Path(__file__).parent
HTML = ROOT.joinpath('data', 'sample.html')
JSON = ROOT.joinpath('data', 'sample.json')


def loads(path):
    with open(path) as f:
        return json.loads(f.read())


def text(path):
    with open(path) as f:
        return f.read()


def test_from_file():
    data = html_to_json.from_file(HTML)

    assert data == loads(JSON)


def test_from_text():
    data = html_to_json.from_string(text(HTML))

    assert data == loads(JSON)
