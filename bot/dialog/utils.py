def calculate_dose(data: dict) -> str:
    mode = data["mode"]
    weight = data["weight"]
    asa = data["asa"]
    elderly = data["elderly"]
    obese = data["obese"]

    # Для расчета берём идеальный вес, если ожирение
    adjusted_weight = weight
    if obese:
        height = 170  # Можно расширить вводом роста
        ideal_bmi = 22
        adjusted_weight = (ideal_bmi * (height / 100) ** 2)

    dose = ""
    if mode == "induction":
        if asa == "I-II":
            base = 2.0
        elif asa == "III":
            base = 1.25
        else:
            base = 0.75
        if elderly:
            base *= 0.6
        dose_mg = round(base * adjusted_weight, 1)
        dose = f"{dose_mg} мг (≈ {base} мг/кг)"
    elif mode == "maintenance":
        if asa in ["I-II", "III"]:
            base_range = (4, 8) if asa == "III" else (6, 12)
        else:
            base_range = (3, 6)
        dose = f"{base_range[0]}–{base_range[1]} мг/кг/ч → {round(base_range[0]*adjusted_weight)}–{round(base_range[1]*adjusted_weight)} мг/ч"
    elif mode == "sedation":
        if asa == "IV-V":
            base_range = (0.5, 2)
        else:
            base_range = (1, 3)
        dose = f"{base_range[0]}–{base_range[1]} мг/кг/ч → {round(base_range[0]*adjusted_weight)}–{round(base_range[1]*adjusted_weight)} мг/ч"

    return dose
