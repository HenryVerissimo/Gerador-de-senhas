from flet import Page, ScrollMode

class PageConfigs:
    def __init__(self, page: Page) -> None:
        self.__page = page

    def build(self) -> None:
        self.__page.padding = 0
        self.__page.title = "Gerador de senhas"
        self.__page.window.width = 1280
        self.__page.window.height = 720
        self.__page.window.min_width = 500
        self.__page.window.min_height = 500
        self.__page.scroll = ScrollMode.AUTO
        self.__page.fonts = {
            "PassionOne-Black": "assets/fonts/PassionOne-Black.ttf",
            "PassionOne-Bold": "assets/fonts/PassionOne-Bold.ttf",
            "PassionOne-Regular": "assets/fonts/PassionOne-Regular.ttf"
        }
