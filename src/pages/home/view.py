import flet as ft

from theme import colors

from components.cards import content_card

def home(page: ft.Page):

    async def open_BMI(e):
        await page.push_route("/bmi")

    title = ft.Text("Health Checker", theme_style=ft.TextThemeStyle.HEADLINE_LARGE, color=colors.BLACK, weight=ft.FontWeight.BOLD)
    subtitle = ft.Text("Chese your checker and see how you are!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM, color= colors.BLACK)
    home_page = ft.Column(
                    scroll=ft.ScrollMode.AUTO,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    controls=[
                        title, subtitle,
                        ft.Divider(),
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            content=ft.Row(
                                wrap=True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[content_card(open_BMI)]
                            )
                        ),
                        
                    ]
                )
    return home_page