import flet as ft

from theme import colors

from .controller import controller_off, controller_bmi, controller_body_fat

from components.functionButton import functionbutton
from components.submitButton import submitbutton
from components.lights import light_detail

def home_view(page: ft.Page):
            
    on_click, form_content, result_content  = controller_off()

    title = ft.Text("Body Metrics", theme_style=ft.TextThemeStyle.HEADLINE_LARGE, color=colors.BLACK, weight=ft.FontWeight.BOLD)
    subtitle = ft.Text("Choose a tool and see your results!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM, color= colors.BLACK)
    form_screen = ft.Container(
        width=400,
        height=500,
        content=form_content,
        border=ft.border.all(20, colors.GRAY_LIGHT),
        border_radius=12,
        bgcolor=colors.SAINT_DEEP_BLACK,
        shadow=ft.BoxShadow(
            blur_radius=1,
            spread_radius=4,
            color=ft.Colors.with_opacity(1, colors.LEADBELCHER),
            offset=ft.Offset(-2, 2),
        )
    )
    result_screen = ft.Container(
        width=400,
        height=300,
        border_radius=12,
        content=result_content,
        bgcolor=colors.SAINT_DEEP_BLACK,
        shadow=ft.BoxShadow(
            blur_radius=1,
            spread_radius=3,
            color=ft.Colors.with_opacity(1, colors.SCAB_RED),
            offset=ft.Offset(3, -3),
            blur_style=ft.BlurStyle.SOLID,
        )
    )
    selection_screen = ft.Container(
        alignment=ft.Alignment.CENTER,
        width=100,
        height=40,
        border_radius=12,
        content=ft.Text(""),
        bgcolor=colors.SAINT_DEEP_BLACK,
    )
    submit_btn = submitbutton(on_click)

    def choose(num):
        nonlocal on_click, form_content, result_content
        match num:
            case 1:
                on_click, form_content, result_content = controller_bmi(page)
                selection_screen.content = ft.Text("BMI")
            case 2: 
                on_click, form_content, result_content = controller_body_fat()
                selection_screen.content = ft.Text("BodyFat")
            case _:
                print("Valor invalido")

        form_screen.content = form_content
        result_screen.content = result_content
        submit_btn.on_click = on_click
        page.update()

    info_card = ft.Container(
                    border_radius=10,
                    padding=16,
                    bgcolor=colors.ALL_SYSTEMS_RED,
                    width=400,
                    height=650,
                    shadow=ft.BoxShadow(
                        blur_radius=1,
                        spread_radius=4,
                        color=ft.Colors.with_opacity(1, colors.SCAB_RED),
                        offset=ft.Offset(-4, 4),
                        blur_style=ft.BlurStyle.SOLID,
                    ),
                    content=
                        ft.Column(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[light_detail(),form_screen,
                                submit_btn
                            ]
                        )
                    )

    result_card = ft.Container(
                    border_radius=10,
                    padding=16,
                    bgcolor=colors.ALL_SYSTEMS_RED,
                    width=400,
                    height=550, 
                    shadow=ft.BoxShadow(
                        blur_radius=1,
                        spread_radius=0,
                        color=ft.Colors.with_opacity(1, colors.SCAB_RED),
                        offset=ft.Offset(0, 8),
                        blur_style=ft.BlurStyle.SOLID,
                    ),
                    content=
                        ft.Column(
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                result_screen,
                                ft.Row(
                                        wrap=True,
                                        spacing=0,
                                        run_spacing=0,
                                        controls=[
                                            functionbutton(lambda _:choose(1), "BMI"),
                                            functionbutton(lambda _:choose(2), "BF"),
                                            functionbutton(lambda _:print("Não Implementado"), ""),
                                            functionbutton(lambda _:print("Não Implementado"), ""),
                                            functionbutton(lambda _:print("Não Implementado"), ""),
                                            functionbutton(lambda _:print("Não Implementado"), ""),
                                            functionbutton(lambda _:print("Não Implementado"), ""),
                                            functionbutton(lambda _:print("Não Implementado"), ""),
                                            functionbutton(lambda _:print("Não Implementado"), ""),
                                            functionbutton(lambda _:print("Não Implementado"), ""),
                               
                                        ]
                                    ),
                                selection_screen
                            ]
                        )
                    )
    



    home = ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY, 
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[  ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[title,subtitle]),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.END,
                                    spacing=0,
                                    controls=[info_card,result_card       
                                    ]
                                )
                            ]
                )
            

    return home