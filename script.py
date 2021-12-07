from flask import Flask, request, render_template, redirect, url_for
from dowg_function import dow

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST", "GET"])
def dayOfWeek():
    if request.method  == "POST":
        date = request.form["date"]
        day = dow(date)
        if day == "Invalid input, try again":
            if len(date) < 1:
                res = render_template("invalid_input.html", dy=day)
                return res
            else:
                res = render_template("invalid_input.html", dte=date, punctuation=":", dy=day)
                return res
        else:
            res = render_template("valid_input.html", dy=day, dte=date, color='style="color: blue"')
            return res


#if __name__ == "__main__":
#    app.run(debug=True)
