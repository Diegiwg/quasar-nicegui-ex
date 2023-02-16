from nicegui.element import Element


class content:
    def __init__(self, parent: Element):
        self.parent = parent

    def icon(self, icon: str) -> None:
        """[icon]: String

        Description: Icon name following Quasar convention; Make sure you have the icon library installed unless you are using 'img:' prefix; If 'none' (String) is used as value then no icon is rendered (but screen real estate will still be used for it)

        Examples: [map] [ion-add] [img:https://cdn.quasar.dev/logo-v2/svg/logo.svg] [img:path/to/some_image.png]"""
        self.parent._props["icon"] = icon


class style:
    def __init__(self, parent: Element) -> None:
        self.parent = parent

    def size(self, size: str) -> None:
        """[size]: String

        Description: Size in CSS units, including unit name or standard size name (xs|sm|md|lg|xl)

        Examples: [16px] [2rem] [xs] [md]"""
        self.parent._props["size"] = size

    def font_size(self, font_size: str) -> None:
        """[font-size]: String

        Description: The size in CSS units, including unit name, of the content (icon, text)

        Examples: [18px] [2rem]"""
        self.parent._props["font-size"] = font_size

    def color(self, color: str) -> None:
        """[color]: String

        Description: Color name for component from the Quasar Color Palette

        Examples: [primary] [teal-10]"""
        self.parent._props["color"] = color

    def text_color(self, text_color: str) -> None:
        """[text-color]: String

        Description: Overrides text color (if needed); Color name from the Quasar Color Palette

        Examples: [primary] [teal-10]"""
        self.parent._props["text-color"] = text_color

    def square(self, square: bool) -> None:
        """[square]: Boolean

        Description: Removes border-radius so borders are squared"""
        self.parent._props["square"] = square

    def rounded(self, rounded: bool) -> None:
        """[rounded]: Boolean

        Description: Applies a small standard border-radius for a squared shape of the component"""
        self.parent._props["rounded"] = rounded


class QAvatar(Element):
    """The QAvatar component creates a scalable, color-able element that can have text, icon or image within its shape. By default it is circular, but it can also be square or have a border-radius applied to give rounded corners to the square shape."""

    def __init__(self, icon: str = "") -> None:
        """The QAvatar component creates a scalable, color-able element that can have text, icon or image within its shape. By default it is circular, but it can also be square or have a border-radius applied to give rounded corners to the square shape."""
        super().__init__("q-avatar")
        self._props["icon"] = icon

        self.qcontent = content(self)
        self.qstyle = style(self)
