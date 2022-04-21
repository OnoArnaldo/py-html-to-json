import html_to_json
from tests.utils import ROOT, loads, text

HTML = ROOT.joinpath('data', 'sample_with_breakline.html')
JSON = ROOT.joinpath('data', 'sample_with_breakline.json')


def test_values_with_breakline():
    data = html_to_json.from_file(HTML)

    import json
    print(json.dumps(data, indent=2))

    assert data == loads(JSON)
