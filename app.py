import flet as ft

from src.configs import PageConfigs, DarkThemeConfigs
from src.views import LoginView, HomeBarView, HomeView, MenuView
from utils import go_to_view, save_password, reload_password, copy_password, config_password

class MyApplication:
    def __init__(self) -> None:
        self.__page: ft.Page = None
        self._colors: dict = None        
        self._dict_views: dict = None
        self._actual_view: ft.Control = None
        self._characters = {
            "numbers": True,
            "upper": True,
            "lower": False,
            "special": False
        }        

    def main(self, page: ft.Page) -> None:
        self.__page = page
        self.__register_configs()
        self.__set_dict_views()
        self.__set_actual_view(self._dict_views["login"])
        self.__register_on_clicks()
        self.__page.on_resized= lambda e:go_to_view(e, self.__page, self._actual_view, self)

        page.add(self._actual_view.build())
        page.update()

    def run_application(self) -> None:
        ft.app(target=self.main)

    def __register_configs(self, configs=PageConfigs, theme=DarkThemeConfigs) -> None:
        configs(self.__page).build()
        self._colors = theme(self.__page).build()

    def __register_on_clicks(self):
        self._dict_views["login"].enter_button.on_click=lambda e:go_to_view(e, self.__page, self._dict_views["home"], self)
        self._dict_views["menu"].home_bar.return_icon.on_click=lambda e:go_to_view(e, self.__page, self._dict_views["home"], self)
        self._dict_views["menu"].home_bar.menu_icon.on_click=lambda e:go_to_view(e, self.__page, self._dict_views["home"], self)
        self._dict_views["home"].home_bar.return_icon.on_click=lambda e:go_to_view(e, self.__page, self._dict_views["login"], self)
        self._dict_views["home"].home_bar.menu_icon.on_click=lambda e:go_to_view(e, self.__page, self._dict_views["menu"], self)
        self._dict_views["home"].save_button.on_click=lambda e: save_password(e, self.__page, self._colors, self._dict_views["home"])
        self._dict_views["home"].reload_icon.on_click=lambda e: reload_password(e, self.__page, self._colors, self._characters, self._dict_views["home"])
        self._dict_views["home"].copy_icon.on_click=lambda e: copy_password(e, self.__page, self._colors, self._dict_views["home"])
        self._dict_views["menu"].numbers_switch.on_change=lambda e: config_password(e, self.__page, self._dict_views["menu"], self)
        self._dict_views["menu"].upper_switch.on_change=lambda e: config_password(e, self.__page, self._dict_views["menu"], self)
        self._dict_views["menu"].lower_switch.on_change=lambda e: config_password(e, self.__page, self._dict_views["menu"], self)
        self._dict_views["menu"].special_switch.on_change=lambda e: config_password(e, self.__page, self._dict_views["menu"], self)
        self._dict_views["menu"].edit_password_switch.on_change=lambda e: config_password(e, self.__page, self._dict_views["menu"], self)

    def __set_dict_views(self) -> None:
        self._dict_views = {
            "login": LoginView(self.__page, self._colors),
            "home_bar": HomeBarView(self.__page, self._colors),
            "home": HomeView(self.__page, self._colors),
            "menu": MenuView(self.__page, self._colors)
        }

    def __set_actual_view(self, view: object) -> None:
        self._actual_view = view


if __name__ == "__main__":

    app = MyApplication()
    app.run_application()
