import flet as ft

from theme import colors

def appbar(page):

    async def go_to():
        await page.push_route("/")
    
    return ft.AppBar(
            leading=ft.IconButton(ft.Icons.HOME, on_click=go_to),
            title=ft.Text(value=f"{page.title}"),
            bgcolor=colors.CONTRAST_DARK,
            actions=[
                ft.TextField(hint_text="Search For More!", prefix_icon=ft.Icons.SEARCH, focused_border_color=colors.GRAY_LIGHT, cursor_color=colors.GRAY_LIGHT),
            ],
        )