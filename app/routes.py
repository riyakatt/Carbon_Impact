from flask import Flask, render_template, request, redirect
from app import app
from app.emission_model import *
import pandas as pd


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/car_impact", methods=['GET'])
def car_impact():

    return render_template("car_impact.html", 
                            car_make_options=load_make_options(), 
                            car_model_options=load_model_options(), 
                            car_cylinders_options=load_cylinder_options())
@app.route("/car_impact", methods=['POST'])
def car_impact_post():
    try:
        if request.form.get('fuel_type') != None:
            fuel_combo = int(request.form.get('fuel_combo'))
            fuel_type = request.form.get('fuel_type')
            cylinders = int(request.form.get("cylinders"))
            transmission = request.form.get("transmission")
            print(fuel_combo, fuel_type, cylinders, transmission)
            df_co2 = pd.read_csv("app/CO2 Emissions_Canada.csv")
            emissions = predict_emissions(df_co2, fuel_type, fuel_combo, cylinders, transmission)
            print(emissions)
        else:
            make = request.form.get("make")
            model = request.form.get("model")
            cylinders = request.form.get("cylinders")
            transmission = request.form.get("transmission")

            df_co2 = pd.read_csv("app/CO2 Emissions_Canada.csv")
            print( make, model, cylinders, transmission)
            emissions = find_co2_emis(df_co2, make, model, int(cylinders), transmission)

        return render_template('car_impact.html',
                        emission_res=emissions,
                        n_trees= int(emissions/21),
                        car_make_options=load_make_options(), 
                        car_model_options=load_model_options(), 
                        car_cylinders_options=load_cylinder_options())
    except:
        return render_template('car_impact.html', 
                    formError="You chose an invalid car configuration, please try again",
                    car_make_options=load_make_options(), 
                    car_model_options=load_model_options(), 
                    car_cylinders_options=load_cylinder_options())

@app.route("/package_impact")
def package_impact():
    return render_template("package_impact.html")