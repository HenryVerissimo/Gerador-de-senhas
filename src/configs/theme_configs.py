from flet import Page, ThemeMode, Colors

class DarkThemeConfigs:
    def __init__(self, page: Page) -> None:
        self.__page = page

    def build(self) -> None:
        self.__page.theme_mode=ThemeMode.DARK
        self.__page.bgcolor="#171716"
        return {
            "color1": Colors.WHITE,
            "colors2": Colors.AMBER,
            "colors3": Colors.BLUE,
            "colors4": Colors.RED,
            "colors5": Colors.GREEN
        }
