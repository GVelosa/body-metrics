import flet as ft

from theme import colors

from pages.home.view import home_view

def main(page: ft.Page):
    page.title = "Body Metrics"
    page.window.maximized = True

    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                bgcolor = colors.GRAY_LIGHT,
                controls=[
                    home_view(page)
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
