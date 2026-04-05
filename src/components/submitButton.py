import flet as ft

from theme import colors

def submitbutton(on_click):
    return ft.Button(
        width=150,
        height=40,
        content="Submit",
        on_click=on_click,
        style=ft.ButtonStyle(
            bgcolor=colors.PRETTY_TWILIGHT_NIGHT,
            color= colors.WHITE,
            text_style=ft.TextStyle(size=12, weight=ft.FontWeight.W_500),
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(
                    3, color=colors.ELITE_BLUE
                ),
                ft.ControlState.HOVERED: ft.BorderSide(
                    3, color=colors.ENDEAVOUR
                ),
            },
        ),
    )