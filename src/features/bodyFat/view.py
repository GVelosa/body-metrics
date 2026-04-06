import flet as ft

from components.genericTextfield import genericitextfield
from components.genericText import generictext

from theme import colors

def body_fat_form():
    user_height = genericitextfield("Height (CM)", ft.KeyboardType.NUMBER, ft.NumbersOnlyInputFilter())
    user_weight = genericitextfield("Weight (KG)", ft.KeyboardType.NUMBER, ft.NumbersOnlyInputFilter())
    user_age = genericitextfield("Age", ft.KeyboardType.NUMBER, ft.NumbersOnlyInputFilter())
    user_neck = genericitextfield("Neck (CM)", ft.KeyboardType.NUMBER, ft.NumbersOnlyInputFilter())
    user_waist = genericitextfield("Waist (CM)", ft.KeyboardType.NUMBER, ft.NumbersOnlyInputFilter())
    user_hip = genericitextfield("Hip (CM)", ft.KeyboardType.NUMBER, ft.NumbersOnlyInputFilter())
    user_hip.visible = False

    def on_sex_change(e):
        is_female = e.control.value
        user_hip.visible = is_female
        e.control.page.update()

    sex_checkbox = ft.Switch(
        thumb_color= colors.LIME_SHOT,
        track_color=colors.TRUE_GREEN,
        track_outline_color= colors.LIME_SHOT,
        label="Male/Female",
        label_text_style=ft.TextStyle(
            color=colors.LIME_SHOT,
        ),
        value=False,
        on_change=on_sex_change,
    )

    return ft.Container(
        border=ft.border.only(
            top=ft.BorderSide(2, colors.LIME_SHOT),
            bottom=ft.BorderSide(2, colors.LIME_SHOT),
        ),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                sex_checkbox,
                user_height,
                user_weight,
                user_age,
                user_neck,
                user_waist,
                user_hip,
            ]
        )
    ),sex_checkbox, user_height, user_weight, user_age, user_neck, user_waist, user_hip


def body_fat_result():
    height_text = generictext()
    weight_text = generictext()
    age_text = generictext()
    navy_body_fat_text = generictext()
    bmi_body_fat_text = generictext()
    category_text = generictext()

    result = ft.Container(
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
                ft.Row(controls=[generictext("Age:"), age_text]),
                ft.Row(controls=[generictext("Navy Method:"), navy_body_fat_text]),
                ft.Row(controls=[generictext("BMI Method:"), bmi_body_fat_text]),
                ft.Row(controls=[generictext("Category:"), category_text]),
            ]
        )
    )

    return (
        result,
        height_text,
        weight_text,
        age_text,
        navy_body_fat_text,
        bmi_body_fat_text,
        category_text,
    )