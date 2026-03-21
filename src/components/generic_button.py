import flet as ft

from theme import colors

def generic_button(on_click):
    return ft.Button(
        bgcolor=colors.CONTRAT_LIGHT,
        color= colors.BLACK,
        elevation=12,
        content="Submit",
        on_click=on_click
    )