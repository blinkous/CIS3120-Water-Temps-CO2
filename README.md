# Water, Temps & CO2
### CIS3120 Group 1

<img src="https://i.imgur.com/6mut7du.gif" width=100%/>
<!-- <img src="https://i.imgur.com/OV6WE3I.gif" width=100%/> -->

## The Problem
The problem that we are addressing is increasing CO2 emissions and waste production. In 2018, CO2 emissions reached an all time after being pretty steady for a few years (Harvey; Plumer). This uptick in emissions highlights the need for efforts to reduce our carbon footprint and waste production. Our goal is to help the local government lower the carbon footprint in New York by preventing excess waste through conservation.

## The Process & Data Sets
In order to advise the local government on actions to take to reduce our carbon footprint and waste production, we analyzed carbon emission, temperatures, and water consumption data. We used three data sets. The first data set was CO2 Emission data for New York State from the eia.gov website that provided annual data on New York Carbon Dioxide Emissions from 1980 to 2016 resulting from fossil fuel consumption by various sectors (Residential, Commercial, Industrial, Transportation, Electric Power etc). The second data set was annual NYC water consumption from 1979 to 2017 from NYC Open Data. The third data set we used was from weather.gov and contained annual temperatures for Central Park from 1869 to 2018. We included temperatures to correlate CO2 emissions to water consumption with the hypothesis that increased temperatures would lead to higher emissions and water consumption. We postulated that increased CO2 emissions water consumption would indicate greater waste production as well.
In order to analyze the data, we converted the data to CSVs, cleaned it and read it into Pandas dataframes. Once we found the largest common date range, we used it to compare the 3 datasets to find the highs and lows for the measures. Using functions, we translated the information to JavaScript and HTML to create an interactive web page. 

## The Solution
Our solution is a way to predict annual CO2 emissions and water consumption based on yearly average temperature so users may utilize the predictions to take proper actions to conserve resources and reduce waste. The solution comes in the form of a web page that users can use to both view stats on CO2, water consumption, and temperatures and get predictions on future stats. The page accepts user input for an annual temperature and outputs the data for years that had the temperatures within 0.1 degrees along with predictions. The predicted CO2 emissions and water consumption are an average of the years with temperatures within 0.1 degrees of the original.

## How to Use the Program
1. Ensure that you’ve downloaded the following files:
- Water_temps_pandas.py
- my_reading_data.py
- my_create_web_page.py
- monthlyannualtempcentralpark.csv
- new_york_co2_emissions.csv
- Water_Consumption_In_The_New_York_City.csv
- page_end.html
- header.html
2. Run water_temps_pandas.py
- The .py file should open up the page in the default browser; the page is optimized for Google Chrome

## Data Sets
- CO2 Emission Data: https://www.eia.gov/environment/emissions/state/ 
- Water Consumption Data: https://data.cityofnewyork.us/Environment/Water-Consumption-In-The-New-York-City/ia2d-e54m 
- Weather Data: https://www.weather.gov/media/okx/Climate/CentralPark/monthlyannualtemp.pdf 

## Works Cited
Harvey, Chelsea. “CO2 Emissions Reached an All-Time High in 2018.” Scientific American, 6 Dec. 2018. https://www.scientificamerican.com/article/co2-emissions-reached-an-all-time-high-in-2018/ 
Plumer, Brad. “U.S. Carbon Emissions Surged in 2018 Even as Coal Plants Closed.” NYTimes, 8 Jan. 2019. https://www.nytimes.com/2019/01/08/climate/greenhouse-gas-emissions-increase.html
