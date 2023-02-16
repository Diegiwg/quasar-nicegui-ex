from nicegui.element import Element


class content:
    def __init__(self, parent: Element):
        self.parent = parent

    def separator(self, separator: str):
        self.parent._props["separator"] = separator

    def gutter(self, gutter: str):
        self.parent._props["gutter"] = gutter

    def align(self, align: str):
        self.parent._props["align"] = align


class style:
    def __init__(self, parent: Element):
        self.parent = parent

    def active_color(self, active_color: str):
        self.parent._props["active-color"] = active_color

    def separator_color(self, separator_color: str):
        self.parent._props["separator-color"] = separator_color


class contentEl:
    def __init__(self, parent: Element):
        self.parent = parent

    def label(self, label: str):
        self.parent._props["label"] = label

    def icon(self, icon: str):
        self.parent._props["icon"] = icon

    def tag(self, tag: str):
        self.parent._props["tag"] = tag


class navigationEl:
    def __init__(self, parent: Element):
        self.parent = parent

    def href(self, href: str):
        self.parent._props["href"] = href

    def target(self, target: str):
        self.parent._props["target"] = target


class stateEl:
    def __init__(self, parent: Element):
        self.parent = parent

    def disabled(self, disabled: bool):
        self.parent._props["disabled"] = disabled


class QBreadcrumbs(Element):
    def __init__(self):
        super().__init__("q-breadcrumbs")

        self.qcontent = content(self)
        self.qstyle = style(self)


class QBreadcrumbsEl(Element):
    def __init__(self) -> None:
        super().__init__("q-breadcrumbs-el")

        self.qcontent = contentEl(self)
        self.qnavigation = navigationEl(self)
        self.qstate = stateEl(self)
