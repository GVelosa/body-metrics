import flet as ft

from components.genericTextfield import genericitextfield
from components.genericText import generictext

from theme import colors

def bmi_form():
    user_height = genericitextfield("Height (CM)", ft.KeyboardType.NUMBER, ft.NumbersOnlyInputFilter())
    user_weight = genericitextfield("Weight (KG)", ft.KeyboardType.NUMBER, ft.NumbersOnlyInputFilter()) 

    return ft.Container(
                border=ft.border.only(
                            top=ft.BorderSide(2, colors.LIME_SHOT),
                            bottom=ft.BorderSide(2, colors.LIME_SHOT),
                        ),
                    content=
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                user_height, user_weight,
                            ]
                        )
                    ), user_height, user_weight

def bmi_result():
    height_text = generictext()
    weight_text = generictext()
    bmi_text = generictext()
    obesity_degree = generictext()
    obesity_classification = generictext()

    bmi_result = ft.Container(
        border=ft.border.only(
                    top=ft.BorderSide(2, colors.LIME_SHOT),
                    bottom=ft.BorderSide(2, colors.LIME_SHOT),
                ),
        padding=50,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(controls=[generictext("Height:"), height_text]),
                ft.Row(controls=[generictext("Weight:"), weight_text]),
                ft.Row(controls=[generictext("BMI:"), bmi_text]),
                ft.Row(controls=[generictext("Classification:"), obesity_classification]),
                ft.Row(controls=[generictext("Degree:"), obesity_degree]),
            ]
        )
    )

    return (
        bmi_result,
        height_text,
        weight_text,
        bmi_text,
        obesity_classification,
        obesity_degree
    )