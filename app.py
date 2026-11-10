from flask import Flask, render_template, request
from calculations import parse_split, format_split, watts_from_split

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            split = parse_split(request.form["split"])
            distance = float(request.form["distance"])
            if split <= 0 or distance <= 0:
                raise ValueError
            result = {
                "split": format_split(split),
                "watts": round(watts_from_split(split)),
                "finish_time": format_split(split * distance / 500),
                "distance": int(distance),
            }
        except ValueError:
            error = "Enter a split like 1:47.5 and a distance in meters."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)