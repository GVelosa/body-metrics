import flet as ft

from theme import colors

from components.appbar import appbar

from pages.home.view import home
from pages.bmi.view import bmi

def main(page: ft.Page):
    page.title = "Body Metrics"
    page.window.maximized = True

    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar= appbar(page),
                bgcolor = colors.GRAY_LIGHT,
                controls=[
                    home(page)
                ],
            )
        )

        if page.route == "/bmi":
            page.views.append(
                ft.View(
                    route="/bmi",
                    appbar= appbar(page),
                    bgcolor = colors.GRAY_LIGHT,
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
