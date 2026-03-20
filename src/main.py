import flet as ft

from theme import colors

from pages.home import home
from pages.bmi import bmi

def main(page: ft.Page):
    page.title = "Financial Analytics"
    page.window.width = 1792
    page.window.height = 1008

    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar= None,
                bgcolor = colors.WHITE,
                controls=[
                    home(page)
                ],
            )
        )

        if page.route == "/imc":
            page.views.append(
                ft.View(
                    route="/imc",
                    appbar= None,
                    bgcolor = colors.WHITE,
                    controls=[
                        bmi(page)
                    ],
                )
            )

        page.update()
    async def view_pop(e):
        if e.view is not None:
            print("View pop:", e.view)
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()
if __name__ == "__main__":
    ft.run(main)
