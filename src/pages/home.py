import flet as ft

from components.cards import content_card

def home(page: ft.Page):

    async def open_IMC(e):
        await page.push_route("/imc")

    title = ft.Text("Health Checker", theme_style=ft.TextThemeStyle.HEADLINE_LARGE)
    subtitle = ft.Text("Chese your checker and see how you are!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)
    home_page = ft.Column(
                    controls=[
                        title, subtitle,
                        content_card(open_IMC)
                    ]
                )
    return home_page