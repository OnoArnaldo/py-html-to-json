from html.parser import HTMLParser

EMPTY_ELEMENTS = (
    'area',
    'base',
    'br',
    'col',
    'embed',
    'hr',
    'img',
    'input',
    'keygen',
    'link',
    'meta',
    'param',
    'source',
    'track',
    'wbr',
    '',
)


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.stack = []
        self.root = {}

    @property
    def stack_size(self) -> int:
        return len(self.stack)

    def append_child(self, new_element: dict) -> None:
        if 0 < self.level <= self.stack_size:
            parent = self.stack[self.level - 1]
            parent['children'].append(new_element)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        new_element = {'tag': tag, 'attributes': dict(attrs), 'value': '', 'children': []}

        if tag not in EMPTY_ELEMENTS:
            if self.level == 0:
                self.root = new_element
            else:
                self.append_child(new_element)

            self.stack.append(new_element)
            self.level += 1
        else:
            self.append_child(new_element)

    def handle_endtag(self, tag: str) -> None:
        if tag not in EMPTY_ELEMENTS:
            self.level -= 1
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if data.strip() != '':
            if 0 < self.level <= len(self.stack):
                parent = self.stack[self.level - 1]
                if len(parent['value']) == 0:
                    self.stack[self.level - 1]['value'] = data.strip()
                else:
                    self.stack[self.level - 1]['value'] += ' ' + data.strip()
