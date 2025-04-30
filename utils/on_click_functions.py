import string
from random import sample
import pyperclip

from flet import Page, ControlEvent
from src.controllers.passwords_controller import PasswordsController
from time import sleep

def go_to_view(e: ControlEvent, page: Page, view: object, app:object) -> None:
    page.clean()
    page.controls.append(view.build())
    app._actual_view = view
    page.update()


def save_password(e:ControlEvent, page: Page, colors:dict, view:object) ->None:
    if view.box_text.value.strip() == "":
        view.save_button.bgcolor = colors["color5"]
        view.text_info.value = "Campo de senha vazio!"
        view.text_info.visible = True

    else:
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


def reload_password(e: ControlEvent, page: Page, colors: dict, characters:dict, view: object) -> None:
    password_char = ""

    if characters["numbers"] == characters["upper"] == characters["lower"] == characters["special"] == False:
        view.text_info.value = "Você precisa selecionar pelo menos um tipo de caractere nas configurações!"
        view.box_text.value = ""
        view.reload_icon.icon_color = colors["color5"]
        view.text_info.visible = True
        page.update()

        sleep(2)
        view.reload_icon.icon_color = colors["color1"]
        view.text_info.value = ""
        view.text_info.visible = False
        page.update()
        return None

    if characters["numbers"]:
        password_char += string.digits

    if characters["upper"]:
        password_char += string.ascii_uppercase

    if characters["lower"]:
        password_char += string.ascii_lowercase

    if characters["special"]:
        password_char += string.punctuation

    password_char = list(password_char)
    password = sample(password_char, 10)
    view.box_text.value = "".join(password)
    view.reload_icon.icon_color = colors["color3"]
    page.update()

    sleep(0.3)
    view.reload_icon.icon_color = colors["color1"]
    page.update()

def copy_password(e: ControlEvent, page: Page, colors: dict, view: object) -> None:

    if view.box_text.value == "":
        view.copy_icon.icon_color = colors["color5"]
        view.text_info.value = "O campo está vazio! nada foi copiado..."
        view.text_info.visible = True

    else:
        password = str(view.box_text.value)
        pyperclip.copy(password)

        view.copy_icon.icon_color = colors["color3"]
        view.text_info.value = "Copiado para área de transferência"
        view.text_info.visible = True

    page.update()

    sleep(2)
    view.copy_icon.icon_color = colors["color1"]
    view.text_info.value = ""
    view.text_info.visible = False
    page.update()

def config_password(e: ControlEvent, page: Page, view: object, app:object) -> None:
    if e.control.label == "Números":
        app._characters["numbers"] = view.numbers_switch.value

    elif e.control.label == "Letras maíusculas":
        app._characters["upper"] = view.upper_switch.value

    elif e.control.label == "Letras minúsculas":
        app._characters["lower"] = view.lower_switch.value
    
    elif e.control.label == "Caracteres especiais":
        app._characters["special"] = view.special_switch.value

    elif e.control.label == "Editar senha":
        app._dict_views["home"].box_text.disabled = not view.edit_password_switch.value

    page.update()