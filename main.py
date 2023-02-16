from nicegui import ui

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


ui.run(title="Quasar Example")
