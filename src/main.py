import flet as ft

from theme import colors

from pages.home.view import home_view

def main(page: ft.Page):
    page.title = "Body Metrics"
    page.window.maximized = True
    page.width = 1920
    page.height = 1080

    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                bgcolor = colors.WHITE,
                padding=0,
                controls=[
                ft.Stack(
                    controls=[
                        ft.Image(
                            src="bg_pokemon.png",
                            width=page.width,
                            height=page.height,
                            fit=ft.BoxFit.COVER,
                            expand=True,
                        ),
                        home_view(page),  # seu conteúdo por cima
                    ],
                expand=True,
                ),
                ] 
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
