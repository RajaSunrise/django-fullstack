from typing import Dict

Tag = str

class TagGenerator:
    @staticmethod
    def script(src: str, attrs: Dict[str, str]) -> Tag:

        attrs_str = " ".join([f'{key}="{value}"' for key, value in attrs.items()])

        return f'<script {attrs_str} src="{src}"></script>'

    @staticmethod
    def stylesheet(href: str) -> Tag:

        return f'<link rel="stylesheet" href="{href}" />'

    @staticmethod
    def stylesheet_preload(href: str) -> Tag:

        return f'<link rel="preload" href="{href}" as="style" />'

    @staticmethod
    def preload(href: str, attrs: Dict[str, str]) -> Tag:
        attrs_str = " ".join([f'{key}="{value}"' for key, value in attrs.items()])
        return f'<link href="{href}" {attrs_str} />'
