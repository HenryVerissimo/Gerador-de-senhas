import flet as ft
from .home_bar_view import HomeBarView

class MenuView:
    def __init__(self, page: ft.Page, colors: dict) -> None:
        self.__page = page
        self._colors = colors
        self.home_bar = HomeBarView(self.__page, self._colors)
        self.text = ft.Text(value="CONFIGURAÇÔES DE SENHA", size=30, font_family="PassionOne-Bold")
        self.numbers_switch = ft.Switch(label="Números", value=True)
        self.upper_switch = ft.Switch(label="Letras maíusculas", value=True)
        self.lower_switch = ft.Switch(label="Letras minúsculas", value=False)
        self.special_switch = ft.Switch(label="Caracteres especiais", value=False)
        self.edit_password = ft.Switch(label="Editar senha", value=False)
        self.passwords_button = ft.Button(text="VER SENHAS SALVAS", icon=ft.Icons.SAVE)

    def build(self) -> None:
        return ft.Container(
            height=self.__page.height,
            content=ft.ResponsiveRow(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            self.home_bar.build(),
                            ft.Container(
                                padding=ft.Padding(left=50, right=50, top=50, bottom=150),
                                content=ft.Column(
                                    controls=[
                                        self.text,
                                        self.numbers_switch,
                                        self.upper_switch,
                                        self.lower_switch,
                                        self.special_switch,
                                        self.edit_password
                                    ]
                                )
                            ),
                            ft.Container(
                                content=self.passwords_button
                            )
                        ]
                    )
                ]
            )
        )