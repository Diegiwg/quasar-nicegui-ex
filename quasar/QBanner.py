from nicegui.element import Element


class content:
    def __init__(self, parent: Element):
        self.parent = parent

    def inline_actions(self, inline_actions: bool):
        self.parent._props["inline-actions"] = inline_actions


class style:
    def __init__(self, parent: Element):
        self.parent = parent

    def dense(self, dense: bool):
        self.parent._props["dense"] = dense

    def rounded(self, rounded: bool):
        self.parent._props["rounded"] = rounded

    def dark(self, dark: bool):
        self.parent._props["dark"] = dark


class QBanner(Element):
    def __init__(self) -> None:
        super().__init__("q-banner")

        self.qcontent = content(self)
        self.qstyle = style(self)
