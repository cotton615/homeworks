import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    page.window_height = '500'
    page.window_width = '500'
    page.title = 'Increment Counter'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'light'

    text_number: TextField = TextField(value='0', text_align=ft.TextAlign.CENTER, width=100) 
    input_number: TextField = TextField(value='1', text_align=ft.TextAlign.CENTER, width=100)
    def decrement(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - str(input_number.value))
        page.update()

    def increment(e: ControlEvent) -> None:
        text_number.value = int(text_number.value) + int(input_number.value)
        page.update()

    def input_num(e: ControlEvent) -> None:
        input_number.value = str(int(input_number.value))
        page.update()

    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=decrement),
            text_number, 
            ft.IconButton(ft.icons.ADD, on_click=increment),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
            input_number,
            ],
            alignment=ft.MainAxisAlignment.CENTER
    )
        )
        

if __name__ == '__main__':
    ft.app(target=main)
