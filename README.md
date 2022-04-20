# html_to_json

HTML converter to JSON which keeps the tag order.

## installation

```shell
python3.10 -m venv venv
source venv\bin\activate

pip install --upgrade pip
pip install git+https://github.com/OnoArnaldo/py-html-to-json.git
```

for development:

```shell
pip install --no-deps -e .
```

## data structure

Every element can have multiple children and has the following structure.

```json
{
  "tag": "tag-name",
  "attributes": {"attribute-name": "attribute-value"},
  "value": "the-value",
  "children": [ <list-of-elements> ]
}
```

## usage

```python
import json
import html_to_json

data = html_to_json.from_file('/path/to/file.html')
data = html_to_json.from_string('<html>'
                                '<head></head>'
                                '<body>'
                                '<img src="/image.jpg">'
                                '<p class="comment">some message</p>'
                                '</body>'
                                '</html>')

print(json.dumps(data, indent=2))
```

result:
```json
{
  "tag": "html",
  "attributes": {},
  "value": "",
  "children": [
    {
      "tag": "head",
      "attributes": {},
      "value": "",
      "children": []
    },
    {
      "tag": "body",
      "attributes": {},
      "value": "",
      "children": [
        {
          "tag": "img",
          "attributes": {
            "src": "/image.jpg"
          },
          "value": "",
          "children": []
        },
        {
          "tag": "p",
          "attributes": {
            "class": "comment"
          },
          "value": "some message",
          "children": []
        }
      ]
    }
  ]
}
```