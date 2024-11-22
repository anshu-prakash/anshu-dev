from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/test")
def test():
    return jsonify({"status": "success"})


@app.route("/")
def about():
    return render_template("about/about.html")


if __name__ == "__main__":
    app.run(debug=True)
