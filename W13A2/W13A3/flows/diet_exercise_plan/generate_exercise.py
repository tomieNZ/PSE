import os
from openai import OpenAI
from promptflow.core import tool


@tool
def generate_exercise(bmi: str, category: str, age: int, gender: str) -> str:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
    )

    prompt = f"""Patient profile:
- BMI: {bmi} ({category})
- Age: {age} years old
- Gender: {gender}

Create a structured 4-week exercise plan.
Tailor the intensity, type, and frequency to this patient's BMI category, age, and gender.

Guidelines:
- Underweight (especially young): progressive strength/resistance training to build muscle, light cardio
- Normal: balanced mix of cardio and strength training
- Overweight (especially older): low-impact cardio (walking, swimming, cycling), light resistance, avoid joint strain

Format the output in markdown with Week 1–4 as headers. For each week list daily activities with duration and intensity."""

    response = client.chat.completions.create(
        model="anthropic/claude-sonnet-4-5",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a certified fitness trainer and exercise physiologist. "
                    "Provide safe, progressive, and realistic exercise plans."
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
