import os
from openai import OpenAI
from promptflow.core import tool

SYSTEM_PROMPT = """\
You are Coach Mike Rivera, a certified fitness trainer and exercise physiologist with 12 years \
of experience designing safe, progressive training programmes. You write in a motivating, \
clear, and structured tone. You always specify exact durations, sets/reps, rest periods, \
and intensity levels (light / moderate / vigorous). Your plans account for the patient's \
age, injury risk, and fitness baseline."""

FEW_SHOT_EXAMPLE = """\
Here is an example of how you format a weekly plan:

## Week 1 — Getting Started (Low Intensity)

**Goal:** Build a consistent exercise habit, assess baseline fitness, avoid injury.

| Day | Activity | Duration | Intensity | Details |
|-----|----------|----------|-----------|---------|
| Mon | Brisk Walking | 30 min | Light | Flat terrain, comfortable pace (~5 km/h) |
| Tue | Bodyweight Strength | 25 min | Light | 2 sets x 10 reps: squats, wall push-ups, glute bridges, planks (20s hold) |
| Wed | Rest / Light Stretching | 15 min | Very Light | Full-body flexibility routine |
| Thu | Brisk Walking | 30 min | Light–Moderate | Include 2 gentle inclines |
| Fri | Bodyweight Strength | 25 min | Light | Same as Tue, aim for improved form |
| Sat | Swimming or Cycling | 20 min | Light | Low-impact cardio alternative |
| Sun | Rest | — | — | Full recovery day |

> *Why this works:* Starting with low-intensity sessions prevents joint strain for an \
older individual while building cardiovascular endurance and muscle memory.\
"""


@tool
def generate_exercise(bmi: str, category: str, age: int, gender: str) -> str:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
    )

    prompt = f"""\
**Patient Profile:**
- BMI: {bmi} ({category})
- Age: {age} years old
- Gender: {gender}

**Task:** Create a structured 4-week progressive exercise plan customised to this patient.

**Requirements:**
1. Each week should have a theme and progressive intensity (e.g. Week 1 low → Week 4 moderate)
2. Use a 7-day table format (Mon–Sun) with columns: Day, Activity, Duration, Intensity, Details
3. Include a mix of cardio and strength exercises appropriate for the patient's profile:
   - Underweight + young: emphasise strength/resistance training (3–4 days), moderate cardio (2 days)
   - Normal: balanced 50/50 split of cardio and strength
   - Overweight + older: prioritise low-impact cardio (walking, swimming, cycling), light resistance, joint-friendly movements
4. Specify exact sets, reps, and rest periods for strength exercises
5. Include at least 1–2 rest or active recovery days per week
6. Add a brief "Why this works" note at the end of each week explaining the physiological reasoning

{FEW_SHOT_EXAMPLE}

Now generate the complete 4-week plan for this patient. \
Use the exact same formatting style and table layout as the example above. \
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
