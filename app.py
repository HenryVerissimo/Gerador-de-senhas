import flet as ft

from src.configs import PageConfigs, DarkThemeConfigs

class MyApplication:
    def __init__(self) -> None:
        self.__page: ft.Page = None
        self.__colors: dict = None        
        self.__dict_views: dict = None
        self.__actual_view: ft.Control = None

    def main(self, page: ft.Page) -> None:
        self.__page = page
        self.__register_configs()

        page.add()
        page.update()

    def run_application(self) -> None:
        ft.app(self.main)

    def __register_configs(self, configs=PageConfigs, theme=DarkThemeConfigs) -> None:
        configs(self.__page).build()
        self.__theme_colors = theme(self.__page).build()

    def __register_views(self) -> None:
        self.__dict_views = {
            {}
        }


if __name__ == "__main__":

    app = MyApplication()
    app.run_application()
