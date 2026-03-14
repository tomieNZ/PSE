import os
from openai import OpenAI
from promptflow.core import tool

SYSTEM_PROMPT = """\
You are Dr. Sarah Chen, a certified clinical nutritionist with 15 years of experience \
in personalised meal planning. You write in a warm, encouraging, and professional tone. \
You always include specific portion sizes (in grams or cups), estimated daily calorie \
targets, and brief reasoning for why certain foods are chosen. \
Your plans are practical for someone with limited cooking skills and a moderate grocery budget."""

FEW_SHOT_EXAMPLE = """\
Here is an example of how you format a weekly plan:

## Week 1 — Foundation Phase (~2,800 kcal/day)

**Goal:** Establish consistent eating habits with calorie-dense, nutrient-rich meals.

**Sample Daily Meal Plan:**

- **Breakfast (7:00 AM):** Oatmeal (80g dry) with whole milk, 1 banana, 2 tbsp peanut butter, \
drizzle of honey (~650 kcal)
- **Mid-morning Snack (10:00 AM):** Greek yoghurt (200g) with mixed nuts (30g) and granola (~350 kcal)
- **Lunch (12:30 PM):** Grilled chicken breast (150g) with brown rice (1 cup cooked), steamed \
broccoli, olive oil dressing (~600 kcal)
- **Afternoon Snack (3:30 PM):** Whole-wheat toast (2 slices) with avocado and 2 boiled eggs (~450 kcal)
- **Dinner (6:30 PM):** Salmon fillet (150g), sweet potato (200g), mixed salad (~550 kcal)
- **Evening Snack (9:00 PM):** Protein smoothie with banana, milk, oats (~300 kcal)

> *Why this works:* Spreading meals across 6 eating windows prevents fullness-related \
discomfort and ensures sustained energy for a young active person.\
"""


@tool
def generate_diet(bmi: str, category: str, age: int, gender: str) -> str:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
    )

    prompt = f"""\
**Patient Profile:**
- BMI: {bmi} ({category})
- Age: {age} years old
- Gender: {gender}

**Task:** Create a structured 4-week diet plan customised to this patient.

**Requirements:**
1. Each week should have a theme/goal (e.g. "Foundation Phase", "Calorie Adjustment", etc.)
2. Include specific foods with portion sizes and estimated calorie counts per meal
3. Provide 6 eating occasions per day: breakfast, mid-morning snack, lunch, afternoon snack, dinner, evening snack
4. Add a brief "Why this works" note at the end of each week explaining the nutritional reasoning
5. Adjust total daily calories based on the BMI category:
   - Underweight: ~2,500–3,000 kcal/day (calorie surplus for weight gain)
   - Normal: ~2,000–2,400 kcal/day (maintenance)
   - Overweight: ~1,400–1,800 kcal/day (moderate deficit for weight loss)
6. Consider age and gender when selecting food types and portions

{FEW_SHOT_EXAMPLE}

Now generate the complete 4-week plan for this patient. \
Use the exact same formatting style as the example above. \
Start directly with "## Week 1" — do not repeat the patient profile."""

    response = client.chat.completions.create(
        model="anthropic/claude-sonnet-4-5",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
        top_p=0.85,
        max_tokens=3000,
        frequency_penalty=0.3,
        presence_penalty=0.1,
        stop=["---END---"],
    )
    return response.choices[0].message.content
