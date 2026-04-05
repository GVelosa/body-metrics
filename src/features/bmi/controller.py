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

def bmi_calculator(
        user_weight,
        user_height,
        height_text,
        weight_text,
        bmi_text,
        obesity_classification,
        obesity_degree,
        page
    ):

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