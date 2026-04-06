import math

body_fat_table_male = [
    (6, "Essential Fat", "0"),
    (14, "Athletes", "0"),
    (18, "Fitness", "0"),
    (25, "Average", "1"),
    (float("inf"), "Obese", "2"),
]

body_fat_table_female = [
    (14, "Essential Fat", "0"),
    (21, "Athletes", "0"),
    (25, "Fitness", "0"),
    (32, "Average", "1"),
    (float("inf"), "Obese", "2"),
]

def body_fat_calculator(
        user_height,
        user_weight,
        user_age,
        user_neck,
        user_waist,
        user_hip,
        is_male,
        height_text,
        weight_text,
        age_text,
        navy_body_fat_text,
        bmi_body_fat_text,
        category_text,
        page
    ):

    try:
        height = float(user_height.value)
        weight = float(user_weight.value)
        age = int(user_age.value)
        neck = float(user_neck.value)
        waist = float(user_waist.value)

        if is_male:
            navy_fat = round(
                86.010*math.log10(waist-neck)-70.041*math.log10(height)+36.76, 2
            )
        else:
            hip = float(user_hip.value)
            navy_fat = round(
                163.205*math.log10(waist+hip-neck)-97.684*math.log10(height)-78.387, 2
            )

        bmi = weight/((height/100)**2)
        if is_male:
            bmi_fat = round((1.20*bmi)+(0.23*age)-16.2, 2)
        else:
            bmi_fat = round((1.20*bmi)+(0.23*age)-5.4, 2)

        height_text.value = user_height.value
        weight_text.value = user_weight.value
        age_text.value = user_age.value
        navy_body_fat_text.value = f"{navy_fat}%"
        bmi_body_fat_text.value = f"{bmi_fat}%"

        table = body_fat_table_male if is_male else body_fat_table_female
        for limit, classification, _ in table:
            if navy_fat < limit:
                category_text.value = classification
                break

        page.update()

    except ValueError as error:
        print(error)
        print("Valor Inválido!")