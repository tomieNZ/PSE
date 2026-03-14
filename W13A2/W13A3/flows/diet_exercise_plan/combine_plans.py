from promptflow.core import tool


@tool
def combine_plans(diet_plan: str, exercise_plan: str) -> dict:
    return {"diet_plan": diet_plan, "exercise_plan": exercise_plan}
