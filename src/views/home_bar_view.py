import flet as ft

class HomeBarView:
    def __init__(self, page: ft.Page, colors:dict) -> None:
        self.__page = page
        self._colors = colors
        self.return_icon = ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_size=40, icon_color=colors["color0"])
        self.logo_image = ft.Image(src="assets/images/cadeado.png", width=50, height=50)
        self.menu_icon = ft.IconButton(icon=ft.Icons.MENU, icon_size=40, icon_color=colors["color0"])

    def build(self):
        return ft.Container(
            bgcolor=self._colors["color3"],
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    self.return_icon,
                    self.logo_image,
                    self.menu_icon
                ]
            )
        )