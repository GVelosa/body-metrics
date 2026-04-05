import flet as ft

from theme import colors

def functionbutton(on_click, name):
    return ft.Button(
        width=70,
        height=70,
        content=name,
        style=ft.ButtonStyle(
            bgcolor=colors.FANTASY_CONSOLE_SKY,
            color= colors.WHITE,
            text_style=ft.TextStyle(size=12, weight=ft.FontWeight.W_500),
            shape=ft.RoundedRectangleBorder(radius=0),
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(
                    3, color=colors.DARK_IMPERIAL_BLUE
                ),
                ft.ControlState.HOVERED: ft.BorderSide(
                    3, color=colors.ENDEAVOUR
                ),
            },
        ),   
        on_click=on_click
    )