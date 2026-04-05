import flet as ft

from features.bmi.view import bmi_form, bmi_result
from features.bmi.controller import bmi_calculator
from features.bodyFat.view import body_fat_form, body_fat_result

def controller_off():
    form_content = ft.Column(controls=[ft.Text("")])
    result_content = ft.Column(controls=[ft.Text("")])
    on_click = lambda _: print("Off")
    return on_click, form_content, result_content

def controller_bmi(page):
    form_content, user_height, user_weight = bmi_form()
    result_content, height_text, weight_text, bmi_text, obesity_classification, obesity_degree = bmi_result()
    on_click = lambda _: bmi_calculator(
                                        user_weight,
                                        user_height,
                                        height_text,
                                        weight_text,
                                        bmi_text,
                                        obesity_classification,
                                        obesity_degree,
                                        page
                                    )
    return on_click, form_content, result_content

def controller_body_fat():
    body_fat_result_view = body_fat_result()
    body_fat_form_view = body_fat_form()
    on_click = lambda _: print("teste")
    return on_click, body_fat_result_view, body_fat_form_view