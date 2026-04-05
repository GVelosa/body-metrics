import flet as ft

from theme import colors

def light_detail():

    return ft.Column(
        alignment=ft.MainAxisAlignment.END,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.Button("",
                        disabled=True,
                        width=60,
                        height=60,
                        style=ft.ButtonStyle(
                            bgcolor =colors.DAYFLOWER,
                            shape=ft.RoundedRectangleBorder(radius=100),
                            side={
                                ft.ControlState.DEFAULT: ft.BorderSide(
                                    3, color=colors.GREY
                                ),
                            },
                        )
                    ),
                    ft.Button("",
                        disabled=True,
                        width=15,
                        height=15,
                        style=ft.ButtonStyle(
                            bgcolor =ft.Colors.RED,
                            shape=ft.RoundedRectangleBorder(radius=100),
                        )
                    ),
                    ft.Button("",
                        disabled=True,
                        width=15,
                        height=15,
                        style=ft.ButtonStyle(
                            bgcolor =ft.Colors.YELLOW,
                            shape=ft.RoundedRectangleBorder(radius=100),
                        )
                    ),
                    ft.Button("",
                        disabled=True,
                        width=15,
                        height=15,
                        style=ft.ButtonStyle(
                            bgcolor =ft.Colors.GREEN,
                            shape=ft.RoundedRectangleBorder(radius=100),
                        )
                    )
                ]
            )
        ]
    )