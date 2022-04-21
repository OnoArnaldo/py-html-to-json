import html_to_json
from tests.utils import ROOT, loads, text

HTML = ROOT.joinpath('data', 'sample.html')
JSON = ROOT.joinpath('data', 'sample.json')


def test_from_file():
    data = html_to_json.from_file(HTML)

    assert data == loads(JSON)


def test_from_text():
    data = html_to_json.from_string(text(HTML))

    assert data == loads(JSON)
