import flet as ft

from theme import colors

from components.generic_button import generic_button

def bmi(page: ft.Page):

    bmi_table = [
        (16, "Severe Thinness", "0"),
        (17, "Moderate Thinness", "0"),
        (18.5, "Mild Thinness", "0"),
        (25, "Normal", "0"),
        (30, "Overweight", "1"),
        (35, "Obese Class I", "1"),
        (40, "Obese Class II", "2"),
        (float("inf"), "Obese Class III", "3"),
    ]

    def bmi_cauculator():
        try:
            weight = float(user_weight.value)
            height = float(user_height.value)
            bmi = round((weight/((height/100) ** 2)), 2)

            height_text.value = user_height.value
            weight_text.value = user_weight.value
            bmi_text.value = str(bmi)
            
            for limit, classification, degree in bmi_table:
                if bmi < limit:
                    obesity_classification.value = classification
                    obesity_degree.value = degree
                    break                                                                                           
                
            page.update()
        except ValueError as error:
            print(error)
            print("Valor Inválido!")

    height_text = ft.Text()
    weight_text = ft.Text()
    bmi_text = ft.Text()
    obesity_degree = ft.Text()
    obesity_classification = ft.Text()

    title = ft.Text("BMI Page", theme_style=ft.TextThemeStyle.HEADLINE_LARGE, color=colors.BLACK)
    user_height = ft.TextField(label="Height(CM)", keyboard_type=ft.KeyboardType.NUMBER,input_filter=ft.NumbersOnlyInputFilter())
    user_weight = ft.TextField(label="Weight(KG)",keyboard_type=ft.KeyboardType.NUMBER,input_filter=ft.NumbersOnlyInputFilter()) 

    info_card = ft.Container(
                    border_radius=10,
                    padding=16,
                    bgcolor=colors.RED_DARK,
                    content=
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                user_height, user_weight,
                                generic_button(bmi_cauculator)
                            ]
                        )
                )
    result_card = ft.Container(
                    border_radius=10,
                    padding=16,
                    bgcolor=colors.RED_DARK,
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
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[info_card,result_card
                                        
                                    ]
                                )
                            ]
                )
            

    return bmi_create