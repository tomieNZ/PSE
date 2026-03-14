from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = round(weight / (height_m ** 2), 2)
    return bmi


def classify_bmi(bmi):
    if bmi < 20:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    else:
        return "Overweight"


@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    weight = ""
    height = ""

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)
        except (ValueError, ZeroDivisionError):
            bmi = None
            category = "Invalid input"

    return render_template("index.html", bmi=bmi, category=category,
                           weight=weight, height=height)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
