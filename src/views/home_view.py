import flet as ft

class HomeView:
    def __init__(self, page: ft.Page, colors: dict) -> None:
        self.__page = page
        self.colors = colors
        self.return_icon = ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_size=40, icon_color=colors["color0"])
        self.logo_image = ft.Image(src="assets/images/cadeado.png", width=50, height=50)
        self.menu_icon = ft.IconButton(icon=ft.Icons.MENU, icon_size=40, icon_color=colors["color0"])
        self.reload_icon = ft.IconButton(icon=ft.Icons.REFRESH, icon_color=colors["color1"])
        self.box_text = ft.TextField(value="")
        self.copy_icon = ft.IconButton(icon=ft.Icons.COPY, icon_color=colors["color1"])
        self.save_button = ft.Button(text="SALVAR", width=150, color=colors["color0"], bgcolor=colors["color3"])
        self.credits_text = ft.Text(value="© Henrique Verissimo")

    def build(self) -> None:
        return ft.Container(
            height=self.__page.height,
            content=ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(
                                bgcolor=self.colors["color3"],
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        self.return_icon,
                                        self.logo_image,
                                        self.menu_icon
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=ft.Padding(left=10, right=10, top=150, bottom=0),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        self.reload_icon,
                                        self.box_text,
                                        self.copy_icon
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=ft.Padding(left=10, right=10, top=0, bottom=10),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        self.save_button
                                    ]
                                )        
                            ),
                            ft.Container(
                                padding=ft.Padding(left=10, right=10, top=10, bottom=10),
                                content=ft.Row(
                                    col=12,
                                    alignment=ft.MainAxisAlignment.END,
                                    controls=[
                                       self.credits_text 
                                    ]    
                                )
                                    
                            )
                        ]
                    )
                ]
            ),

        )