from nicegui import ui
from requests import get

from quasar import *

# Avatar
el_1 = avatar("clock")
el_1.qcontent.icon("directions")
el_1.qstyle.color("pink")

# Badge
el_2 = badge()
el_2.qcontent.label("Hello")
el_2.qcontent.align("center")
el_2.qstyle.color("blue")
el_2.qstyle.outline(True)

# Banner
el_3 = banner()
el_3.qcontent.inline_actions(True)
el_3.qstyle.rounded(True)
el_3.qstyle.dense(False)

with el_3.style(add="background: red; color: white;"):
    ui.label("Hello")
    ui.label("World")

# Bar
el_4 = bar()
el_4.qstyle.dark(True)
el_4.qstyle.dense(True)

with el_4.style(add="background: red; color: white;"):
    ui.label("File")
    ui.label("Edit")
    ui.label("View")
    ui.label("Tools")

# Breadcrumb
el_5 = breadcrumbs()

with el_5:
    el_5_1 = breadcrumbsEl()
    el_5_1.qcontent.label("Home")
    el_5_1.qnavigation.href("/")
    el_5_1.qstate.disabled(True)

    el_5_2 = breadcrumbsEl()
    el_5_2.qcontent.label("File")
    el_5_2.qnavigation.href("/file")
    el_5_1.qnavigation.target("_blank")


# Table
el_6 = table()
el_6.selection.type("single")


el_6.columns.add("title", "Title", "title")
el_6.columns.add("completed", "Completed", "completed")

ui.button("Add ID column", on_click=lambda: el_6.columns.add("id", "id", "id"))


req = get("https://jsonplaceholder.typicode.com/todos")
todos = req.json()

for todo in todos:
    el_6.rows.add(todo)


async def get_element():
    await ui.run_javascript(
        f"window.table = (getElement({el_6.id})); window.table;", respond=False
    )


ui.button("Get element", on_click=get_element)

ui.run(title="Quasar Example")
