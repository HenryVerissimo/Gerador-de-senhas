from flet import Page, ControlEvent
from src.controllers.passwords_controller import PasswordsController
from time import sleep

def go_to_home(e: ControlEvent, page: Page, view: object) -> None:
    page.clean()
    page.controls.append(view.build())
    page.update()

def go_to_login(e: ControlEvent, page: Page, view: object) -> None:
    page.clean()
    page.controls.append(view.build())
    page.update()

def save_password(e:ControlEvent, page: Page, colors:dict, view:object) ->None:
    request = PasswordsController().insert_db(view.box_text.value)

    if not request:
        view.save_button.bgcolor = colors["color5"]
        view.text_info.value = "Essa senha já foi salva!"
        view.text_info.visible = True

    else:    
        view.save_button.bgcolor = colors["color4"]
        view.text_info.value = "Salvo com sucesso!"
        view.text_info.visible = True
           
    page.update()
    sleep(2)

    view.save_button.bgcolor = colors["color3"]
    view.text_info.value = ""
    view.text_info.visible = False
    page.update()
