import flet as ft
import asyncio

from theme import colors

def light_detail():

    async def countdown():
        blue.disabled=True
        blue.update()
        while True:
            red.bgcolor = ft.Colors.RED
            yellow.bgcolor = ft.Colors.YELLOW_700
            green.bgcolor = ft.Colors.GREEN_700
            red.update()
            yellow.update()
            green.update()
            await asyncio.sleep(0.5)
            red.bgcolor = ft.Colors.RED_700
            yellow.bgcolor = ft.Colors.YELLOW
            green.bgcolor = ft.Colors.GREEN_700
            red.update()
            yellow.update()
            green.update()
            await asyncio.sleep(0.5)
            red.bgcolor = ft.Colors.RED_700
            yellow.bgcolor = ft.Colors.YELLOW_700
            green.bgcolor = ft.Colors.GREEN
            red.update()
            yellow.update()
            green.update()
            await asyncio.sleep(0.5)

    
    blue = ft.Button(
                    "",
                    disabled=False,
                    on_click=countdown,
                    width=50,
                    height=50,
                    style=ft.ButtonStyle(
                        bgcolor =colors.FANTASY_CONSOLE_SKY,
                        shape=ft.RoundedRectangleBorder(radius=100),
                        side={
                            ft.ControlState.DEFAULT: ft.BorderSide(
                                3, color=ft.Colors.WHITE_38
                            ),
                        },
                    ),
                )

    red = ft.Button(
                    "",
                    disabled=True,
                    width=15,
                    height=15,
                    style=ft.ButtonStyle(
                        bgcolor =ft.Colors.RED_700,
                        shape=ft.RoundedRectangleBorder(radius=100),
                    ),
                )
    green = ft.Button(
                    "",
                    disabled=True,
                    width=15,
                    height=15,
                    style=ft.ButtonStyle(
                        bgcolor =ft.Colors.GREEN_700,
                        shape=ft.RoundedRectangleBorder(radius=100),
                    )
                )
    yellow = ft.Button(
                    "",
                    disabled=True,
                    width=15,
                    height=15,
                    style=ft.ButtonStyle(
                        bgcolor =ft.Colors.YELLOW_700,
                        shape=ft.RoundedRectangleBorder(radius=100),
                    )
                )
    return ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    blue, red, yellow, green
                    ]
                )