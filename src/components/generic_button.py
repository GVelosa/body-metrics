import flet as ft

def generic_button(on_click):
    return ft.Button(
        content="Submit",
        on_click=on_click
    )