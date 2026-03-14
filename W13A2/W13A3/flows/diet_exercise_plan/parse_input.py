from promptflow.core import tool


@tool
def parse_input(weight: float, height: float, age: int, gender: str) -> dict:
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2)

    if bmi < 20:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    else:
        category = "Overweight"

    return {"bmi": str(bmi), "category": category}
