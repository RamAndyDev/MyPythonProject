from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    # Implement logic to handle user registration
    # (e.g., store user information in a database)

    return render_template("success.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
