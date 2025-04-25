from flet import Page, ControlEvent

def go_to_home(e: ControlEvent, page: Page, view: object) -> None:
    page.clean()
    page.controls.append(view.build())
    page.update()

def go_to_login(e: ControlEvent, page: Page, view: object) -> None:
    page.clean()
    page.controls.append(view.build())
    page.update()