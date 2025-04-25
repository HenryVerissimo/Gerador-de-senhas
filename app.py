import flet as ft

class MyApplication:
    def __init__(self) -> None:
        self.__page: ft.Page = None
        self.__actual_view: ft.Control = None
        self.__dict_views: dict = None

    def main(self, page: ft.Page) -> None:
        self.__page = page
        self.__register_configs()
        self.__register_theme()

        page.add()
        page.update()

    def run_application(self) -> None:
        ft.app(self.main)

    def __register_configs(self, configs) -> None:
        configs(self.__page).build()

    def __register_theme(self) -> None:
        self.__page.theme_mode=ft.ThemeMode.DARK
        self.__page.bgcolor="#171716"

if __name__ == "__main__":

    app = MyApplication()
    app.run_application()
