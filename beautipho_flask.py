from flask import Flask, render_template, redirect, request, send_from_directory, make_response, jsonify, abort,redirect,url_for

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/process")

@app.route("/process")
def process():
    return render_template("process.html")

if __name__ == "__main__":
    app.run(host="10.196.20.58",port=5001,debug=True)
