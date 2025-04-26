from flet import Page, ThemeMode, Colors

class DarkThemeConfigs:
    def __init__(self, page: Page) -> None:
        self.__page = page

    def build(self) -> None:
        self.__page.theme_mode=ThemeMode.DARK
        self.__page.bgcolor="#171716"
        return {
            "color0": Colors.BLACK,
            "color1": Colors.WHITE,
            "color2": Colors.AMBER,
            "color3": Colors.BLUE,
            "color4": Colors.GREEN
        }
