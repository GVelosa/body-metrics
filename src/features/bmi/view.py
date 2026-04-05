import flet as ft

from theme import colors

def bmi_form():
    user_height = ft.TextField(label="Height(CM)", keyboard_type=ft.KeyboardType.NUMBER,input_filter=ft.NumbersOnlyInputFilter())
    user_weight = ft.TextField(label="Weight(KG)",keyboard_type=ft.KeyboardType.NUMBER,input_filter=ft.NumbersOnlyInputFilter()) 

    return ft.Container(
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
    height_text = ft.Text()
    weight_text = ft.Text()
    bmi_text = ft.Text()
    obesity_degree = ft.Text()
    obesity_classification = ft.Text()

    bmi_result = ft.Container(
        content=ft.Column(
            expand=True,
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

    return (
        bmi_result,
        height_text,
        weight_text,
        bmi_text,
        obesity_classification,
        obesity_degree
    )