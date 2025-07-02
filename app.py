from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    table = []
    num = None
    if request.method == "POST":
        try:
            num = int(request.form["number"])
            table = [f"{num} × {i} = {num * i}" for i in range(1, 13)]
        except:
            table = ["Please enter a valid number."]
    return render_template("index.html", table=table, num=num)

if __name__ == "__main__":
    app.run(debug=True)
