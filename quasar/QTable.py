from nicegui.element import Element


class columns:
    itens = []

    def __init__(self, parent: Element) -> None:
        self.parent = parent

    def add(self, name: str, label: str, field: str):
        self.itens.append({"name": name, "label": label, "field": field})
        self.parent.update()


class rows:
    data = []

    def __init__(self, parent: Element) -> None:
        self.parent = parent

    def add(self, data: dict):
        self.data.append(data)
        self.parent.update()


class selection:
    def __init__(self, parent: Element) -> None:
        self.parent = parent
        self.parent._props["selected"] = []

    def type(self, type: str):
        self.parent._props["selection"] = type


class QTable(Element):
    def __init__(self) -> None:
        super().__init__("q-table")

        self.columns = columns(self)
        self._props["columns"] = self.columns.itens

        self.rows = rows(self)
        self._props["rows"] = self.rows.data

        self.selection = selection(self)
