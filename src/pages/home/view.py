import flet as ft

from theme import colors

from .controller import controller_off, controller_bmi, controller_teste

from components.functionButton import functionbutton
from components.submitButton import submitbutton
from components.lights import light_detail

def home_view(page: ft.Page):
            
    on_click, form_content, result_content  = controller_off()

    title = ft.Text("Body Metrics", theme_style=ft.TextThemeStyle.HEADLINE_LARGE, color=colors.BLACK, weight=ft.FontWeight.BOLD)
    subtitle = ft.Text("Choose a tool and see your results!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM, color= colors.BLACK)
    form_screen = ft.Card(
        width=400,
        height=500,
        content=form_content
    )
    result_screen = ft.Card(
        width=400,
        height=350,
        content=result_content
    )
    submit_btn = submitbutton(on_click)

    def choose(num):
        nonlocal on_click, form_content, result_content
        match num:
            case 1:
                on_click, form_content, result_content = controller_bmi(page)
            case 2: 
                on_click, form_content, result_content = controller_teste()
            case _:
                print("Valor invalido")

        form_screen.content = form_content
        result_screen.content = result_content
        submit_btn.on_click = on_click
        page.update()
        print(num)

    info_card = ft.Container(
                    border_radius=10,
                    padding=16,
                    bgcolor=colors.ALL_SYSTEMS_RED,
                    width=400,
                    height=650,
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
                    content=
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[result_screen,
                               ft.Row(
                                    wrap=True,
                                    spacing=0,
                                    run_spacing=0,
                                    controls=[
                                        functionbutton(lambda _:choose(1), "BMI"),
                                        functionbutton(lambda _:choose(2), "Teste")
                                    ]
                                )   
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