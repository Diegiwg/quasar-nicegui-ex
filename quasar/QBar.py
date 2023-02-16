from nicegui.element import Element


class style:
    def __init__(self, parent: Element):
        self.parent = parent

    def dense(self, dense: bool):
        self.parent._props["dense"] = dense

    def dark(self, dark: bool):
        self.parent._props["dark"] = dark


class QBar(Element):
    def __init__(self) -> None:
        super().__init__("q-bar")

        self.qstyle = style(self)
