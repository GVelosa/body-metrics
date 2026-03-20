import flet as ft

from theme import colors

from components.generic_button import generic_button

def bmi(page: ft.Page):
    def bmi_cauculator():
        #Creat Try/Except for nom numerical values
        weight = float(user_weight.value)
        height = float(user_height.value)
        bmi = round((weight/((height/100) ** 2)), 2)
        if bmi < 18.5:
            return print("Magreza", 0)
        elif bmi < 25:
            return print("Normal", 0)
        elif bmi < 30:
            return print("Sobrepeso", 1)
        elif bmi < 40:
            return print("Obesidade", 2)
        else:
            return print("Obesidade Grave", 3)
                
                

    title = ft.Text("BMI Page", theme_style=ft.TextThemeStyle.HEADLINE_LARGE)
    user_height = ft.TextField(label="Height(CM)", keyboard_type=ft.KeyboardType.NUMBER,input_filter=ft.NumbersOnlyInputFilter())
    user_weight = ft.TextField(label="Weight(KG)",keyboard_type=ft.KeyboardType.NUMBER,input_filter=ft.NumbersOnlyInputFilter())    
    submit = generic_button(bmi_cauculator)

    bmi_create = ft.Container(
        border_radius=10,
        padding=16,
        bgcolor = colors.RED_DARK,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                title,
                user_height,
                user_weight,
                submit
            ]
        )
    )

    return bmi_create