import flet as ft

from theme import colors

def content_card(on_click):

    return ft.Card(
        bgcolor = colors.RED_DARK,
        content=ft.GestureDetector(
            on_tap= on_click,
            mouse_cursor = ft.MouseCursor.CLICK,
            content=ft.Container(
                padding=ft.Padding.only(left=16, right=16),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    width=250,
                    height=80,
                    controls=[
                        ft.Icon(ft.Icons.ABC, size=45), 
                        ft.Divider(),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=2,
                            controls=[
                                ft.Text("Name", color=colors.WHITE, weight=ft.FontWeight.BOLD, size=18),
                                ft.Text("Small Description", color=colors.GRAY_LIGHT, size=14)
                            ]
                        )
                    ]
                )
            )
        )
            
    )
        
