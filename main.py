from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", page="home")


if __name__ == "__main__":
    app.run(debug=True)