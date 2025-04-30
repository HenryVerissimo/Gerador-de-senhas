import flet as ft
from .home_bar_view import HomeBarView

class HomeView:
    def __init__(self, page: ft.Page, colors: dict) -> None:
        self.__page = page
        self._colors = colors
        self.text = ft.Text(value="GERADOR DE SENHAS", font_family="PassionOne-Bold", color=colors["color6"], size=40)
        self.home_bar = HomeBarView(self.__page, self._colors)
        self.reload_icon = ft.IconButton(icon=ft.Icons.REFRESH, icon_color=colors["color1"])
        self.box_text = ft.TextField(value="", border_color=colors["color1"], disabled=True)
        self.copy_icon = ft.IconButton(icon=ft.Icons.COPY, icon_color=colors["color1"])
        self.text_info = ft.Text(value="", visible=False, size=20, color=colors["color1"], text_align= ft.TextAlign.CENTER)
        self.save_button = ft.Button(text="SALVAR", width=200, color=colors["color1"], bgcolor=colors["color3"])
        self.credits_text = ft.Text(value="© Henrique Verissimo")

    def build(self) -> None:
        return ft.Container(
            height=self.__page.height,
            content=ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            self.home_bar.build(),
                            ft.Container(
                                padding=ft.Padding(left=10, right=10, top=140, bottom=0),                                
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        self.text
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=ft.Padding(left=10, right=10, top=10, bottom=0),
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
                                padding=ft.Padding(left=10, right=10, top=0, bottom=0),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        self.text_info
                                    ]
                                )        
                            ),
                            ft.Container(
                                padding=ft.Padding(left=10, right=10, top=0, bottom=10),
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