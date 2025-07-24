from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = float(request.form.get("q"))
    # load model
    model = joblib.load("dbs.jl")
    # make prediction
    pred = model.predict([[q]])
    return(render_template("main.html"))

@app.route("/sepia",methods=["GET","POST"])
def sepia():
    return(render_template("sepia_hf.html"))

if __name__ == "__main__":
    app.run()
