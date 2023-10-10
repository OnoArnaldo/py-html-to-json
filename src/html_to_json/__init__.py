import typing as _
from html_to_json.parser import Parser

if _.TYPE_CHECKING:
    from pathlib import Path


def from_file(file_name: 'Path') -> dict:
    p = Parser()

    with open(file_name, encoding='utf8') as f:
        for line in f:
            p.feed(line)

    return p.root


def from_string(string: str) -> dict:
    p = Parser()
    p.feed(string)
    return p.root
