from flask import Flask,render_template,request
import joblib
import numpy as np
app=Flask(__name__)
model=joblib.load("model.pkl")
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        vals=[float(request.form[k]) for k in ["age","sex","cp","trestbps","chol","thalach"]]
        pred=model.predict([vals])[0]
        return render_template("result.html",prediction="Heart Disease" if pred else "No Heart Disease")
    return render_template("index.html")
app.run(debug=True)
