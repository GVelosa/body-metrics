import flet as ft

from theme import colors

def genericitextfield(label, keybordtype=None, filter_exist=None):
    return ft.TextField(
        color=colors.LIME_SHOT,
        border_color=colors.LIME_SHOT,
        label=label, 
        label_style=ft.TextStyle(
            color=colors.CELESTIAL_ALIEN
        ),
        selection_color=colors.LIME_SHOT,
        keyboard_type=keybordtype,
        input_filter=filter_exist,
        cursor_color=colors.CELESTIAL_ALIEN
    )