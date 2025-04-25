import flet as ft

class LoginView:
    def __init__(self, page: ft.Page, colors: dict) -> None:
        self.__page = page
        self.logo_image = ft.Image(src="assets/images/cadeado.png", width=150, height=150)
        self.text1 = ft.Text(value="GERADOR DE ", color=["color1"], font_family="PassionOne-Bold", size=30)
        self.text2 = ft.Text(value="SENHAS", color=colors["color3"], font_family="PassionOne-Bold", size=30)
        self.enter_button = ft.Button(text="ENTAR", width=150, style=ft.ButtonStyle(color=colors["color3"]))

    def build(self) -> None:
        return ft.Container(
            height=self.__page.height,
            content=ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                content=self.logo_image
                            ),
                            ft.Container(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        self.text1,
                                        self.text2
                                    ]
                                )
                            ),
                            ft.Container(
                                content=self.enter_button
                            )
                        ]
                    )
                ]
            )
        )