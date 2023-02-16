from nicegui.element import Element


class content:
    def __init__(self, parent: Element):
        self.parent = parent

    def floating(self, floating: bool):
        self.parent._props["floating"] = floating

    def multi_line(self, multi_line: bool):
        self.parent._props["multi-line"] = multi_line

    def label(self, label: str):
        self.parent._props["label"] = label

    def align(self, align: str):
        self.parent._props["align"] = align


class style:
    def __init__(self, parent: Element):
        self.parent = parent

    def color(self, color: str):
        self.parent._props["color"] = color

    def text_color(self, text_color: str):
        self.parent._props["text-color"] = text_color

    def transparent(self, transparent: bool):
        self.parent._props["transparent"] = transparent

    def outline(self, outline: bool):
        self.parent._props["outline"] = outline

    def rounded(self, rounded: bool):
        self.parent._props["rounded"] = rounded


class QBadge(Element):
    def __init__(self) -> None:
        super().__init__("q-badge")

        self.qcontent = content(self)
        self.qstyle = style(self)
