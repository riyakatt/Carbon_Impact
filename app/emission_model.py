import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def load_make_options():
    f = open('app/car_options_data/makes.pickle','rb')
    makes = sorted(pickle.load(f))
    f.close()
    return makes

def load_model_options():
    f = open('app/car_options_data/models.pickle','rb')
    models = sorted(pickle.load(f))
    f.close()
    return models

def load_cylinder_options():
    f = open('app/car_options_data/cylinders.pickle','rb')
    cylinders = sorted(pickle.load(f))
    f.close()
    return cylinders

def find_co2_emis(df_co2, make: str, model: str, cylinder: int, transmission: str):
    make = make.upper()
    model = model.upper()
    transmission = transmission.lower()
    if len(df_co2[(df_co2['Make'] == make)&(df_co2['Model'] == model) ]) < 1:
        print("Car not found please enter average fuel consumption")
        raise Exception("Car not found please enter average fuel consumption")

    elif len(df_co2[(df_co2['Make'] == make)&(df_co2['Model'] == model) ]) == 1:
        return df_co2[(df_co2['Make'] == make)&(df_co2['Model'] == model) ]['CO2 Emissions(g/km)']
    else:
        #avg them, or also request cylinder and transmission type to make it even more specific.
        #return df_co2[(df_co2['Make'] == make)&(df_co2['Model'] == model) ]['CO2 Emissions(g/km)'].mean()
        subset = df_co2[(df_co2['Make'] == make)&(df_co2['Model'] == model) &(df_co2['Cylinders'] == cylinder)]
        if transmission == 'automatic':
            return subset[subset['Transmission'].str.match("A")]['CO2 Emissions(g/km)'].mean()
        else:
            return subset[subset['Transmission'].str.match("M")]['CO2 Emissions(g/km)'].mean()

def predict_emissions(df_co2, fuelType, fuelCombo, cylinders, transmission):
    emissions = df_co2['CO2 Emissions(g/km)']
    fuelTypes =['diesal', 'ethanol', 'natural gas', 'regular', 'premium']
    adj_df = df_co2.copy()
    encodedType = pd.get_dummies(adj_df['Fuel Type'])
    adj_df.drop(['Model','Make','Vehicle Class','Fuel Type', 'CO2 Emissions(g/km)'], axis  = 1, inplace = True)
    adj_df = adj_df.join(encodedType)
    adj_df['Transmission'] = (adj_df['Transmission'].str.match("A").astype(int))
    if transmission == 'automatic':
      transmission = 1
    else:
      transmission = 0
    fuelCity = fuelCombo*2*0.55
    fuelHwy = fuelCombo*2*0.45
    engSize = df_co2[df_co2['Cylinders'] == cylinders]['Engine Size(L)'].mean()
    fuelMPG = int(282.481/fuelCombo)
    ourSerList = [engSize, cylinders,transmission, fuelCity,fuelHwy, fuelCombo, fuelMPG]
    for i in fuelTypes:
      if fuelType == i:
        ourSerList.append(1)
      else:
        ourSerList.append(0)
    ourSer = pd.Series(ourSerList)
    emissions = np.array(emissions)
    emissions = emissions.reshape(-1,1)
    samp = np.array(ourSer)
    samp = [samp]
    linReg = LinearRegression()
    linReg = linReg.fit(X = np.array(adj_df),y = emissions )
    pred = linReg.predict(samp)
    
    return pred[0][0]
