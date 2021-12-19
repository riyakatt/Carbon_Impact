# Carbon_Impact
*Created for the AYLUS Humanity Hacks Hackathon*

In this project, we hope to motivate people to be more environmentally conscious by visualizing the larger impact of simple parts of our daily routine, like buying groceries and driving your car. 

The app has also been deployed on google cloud app engine at:
Carbon Impact (hackathons-335614.uc.r.appspot.com)

Devpost Submission Link: 
 
 
### Developer Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run the app with `python main.py`
#### Directory Structure
```
app/
    car_options_data/
    static/
    templates/
    __init__.py
    routes.py
    emission_model.py
    CO2 Emissions_Canada.csv
emission_analysis/
    data_analysis.ipynb
main.py
requirements.txt
```
## Working Features
- Active Features:
    - The CO2 Emissions Calculator and Visualization
    - The CO2 Emissions Predictor and Visualization
- Working, but not integrated into web app
    - Graphs Showing Impact over Time compared to Planting a Tree
- Incomplete Features:
    - Food packaging calculator
