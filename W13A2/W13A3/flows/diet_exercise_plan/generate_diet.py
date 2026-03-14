import os
from openai import OpenAI
from promptflow.core import tool


@tool
def generate_diet(bmi: str, category: str, age: int, gender: str) -> str:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
    )

    prompt = f"""Patient profile:
- BMI: {bmi} ({category})
- Age: {age} years old
- Gender: {gender}

Create a structured 4-week diet plan with daily meal suggestions (breakfast, lunch, dinner, snacks).
Tailor calorie targets and food choices specifically to this patient's BMI category, age, and gender.

Guidelines:
- Underweight: high-calorie, protein-rich meals to support healthy weight gain
- Normal: balanced, varied meals to maintain weight
- Overweight: low-calorie, nutrient-dense meals to support gradual weight loss

Format the output in markdown with Week 1–4 as headers. For each week give a sample daily meal plan."""

    response = client.chat.completions.create(
        model="anthropic/claude-sonnet-4-5",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a certified nutritionist. Provide practical, "
                    "realistic meal plans with specific food examples."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
        top_p=0.85,
        max_tokens=2000,
        frequency_penalty=0.3,
        presence_penalty=0.1,
        stop=["---END---"],
    )
    return response.choices[0].message.content
