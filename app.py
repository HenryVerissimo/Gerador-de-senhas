import flet as ft

from src.configs import PageConfigs, DarkThemeConfigs
from src.views import LoginView, HomeView
from utils import go_to_home, go_to_login

class MyApplication:
    def __init__(self) -> None:
        self.__page: ft.Page = None
        self._colors: dict = None        
        self._dict_views: dict = None
        self._actual_view: ft.Control = None

    def main(self, page: ft.Page) -> None:
        self.__page = page
        self.__register_configs()
        self.__set_dict_views()
        self.__set_actual_view(self._dict_views["login"])
        self.__register_on_clicks()

        page.add(self._actual_view.build())
        page.update()

    def run_application(self) -> None:
        ft.app(target=self.main)

    def __register_configs(self, configs=PageConfigs, theme=DarkThemeConfigs) -> None:
        configs(self.__page).build()
        self._colors = theme(self.__page).build()

    def __register_on_clicks(self):
        self._dict_views["login"].enter_button.on_click=lambda e:go_to_home(e, self.__page, self._dict_views["home"])
        self._dict_views["home"].return_icon.on_click=lambda e:go_to_login(e, self.__page, self._dict_views["login"])

    def __set_dict_views(self) -> None:
        self._dict_views = {
            "login": LoginView(self.__page, self._colors),
            "home": HomeView(self.__page, self._colors),
        }

    def __set_actual_view(self, view: object) -> None:
        self._actual_view = view


if __name__ == "__main__":

    app = MyApplication()
    app.run_application()
