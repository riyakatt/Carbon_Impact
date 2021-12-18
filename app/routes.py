from flask import Flask, render_template
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/car_impact")
def car_impact():
    car_make_options = ["Acura", "Toyota", "Hyundai", "Honda", "Audi", "BMW"]
    car_make_options = sorted(car_make_options)
    car_model_options = ["model s", "model 3", "model y", "model x", "roadster"]
    car_make_options = sorted(car_make_options)
    car_model_options = sorted(car_model_options)
    return render_template("car_impact.html", car_make_options=car_make_options, car_model_options=car_model_options)

@app.route("/package_impact")
def package_impact():
    return render_template("package_impact.html")