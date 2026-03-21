import flet as ft

from theme import colors

from .controller import bmi_cauculator
from components.generic_button import generic_button

def bmi(page: ft.Page):
    
    height_text = ft.Text()
    weight_text = ft.Text()
    bmi_text = ft.Text()
    obesity_degree = ft.Text()
    obesity_classification = ft.Text()

    title = ft.Text("BMI Page", theme_style=ft.TextThemeStyle.HEADLINE_LARGE, color=colors.BLACK)
    user_height = ft.TextField(label="Height(CM)", keyboard_type=ft.KeyboardType.NUMBER,input_filter=ft.NumbersOnlyInputFilter())
    user_weight = ft.TextField(label="Weight(KG)",keyboard_type=ft.KeyboardType.NUMBER,input_filter=ft.NumbersOnlyInputFilter()) 

    info_card = ft.Container(
                    expand=,
                    border_radius=10,
                    padding=16,
                    bgcolor=colors.RED,
                    constraints=ft.BoxConstraints(
                        max_width=400,
                        max_height=500
                    ),
                    content=
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                user_height, user_weight,
                                generic_button(
                                    lambda e: bmi_cauculator(
                                        user_weight,
                                        user_height,
                                        height_text,
                                        weight_text,
                                        bmi_text,
                                        obesity_classification,
                                        obesity_degree,
                                        page
                                    )
                                )
                            ]
                        )
                    )
    result_card = ft.Container(
                    border_radius=10,
                    padding=16,
                    bgcolor=colors.RED,
                    content=
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Row(controls=[ft.Text("Height:"), height_text]),
                                ft.Row(controls=[ft.Text("Weight:"), weight_text]),
                                ft.Row(controls=[ft.Text("BMI:"), bmi_text]),
                                ft.Row(controls=[ft.Text("Classification:"), obesity_classification]),
                                ft.Row(controls=[ft.Text("Degree:"), obesity_degree]),
                            ]
                        )
                    )

    bmi_create = ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[  title,
                              ft.Divider(),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    controls=[info_card,result_card       
                                    ]
                                )
                            ]
                )
            

    return bmi_create