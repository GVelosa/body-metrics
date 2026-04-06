import flet as ft

from theme import colors

def generictext(value = ""):
    return ft.Text(
        value=value,
        color=colors.LIME_SHOT
    )