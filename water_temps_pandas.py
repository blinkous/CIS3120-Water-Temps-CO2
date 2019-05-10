import pandas as pd
import my_reading_data as r

# 1: Preparing the data using external script ======================================================================
# Read the csv using functions defined in the my_reading_data.py file
WaterCons_df = r.readWater()
Temps_df = r.readTemp()
CO2_df = r.readCO2()

# Ensure that the data has the same year ranges
lowerBoundYear = r.lowerYearBound(WaterCons_df, Temps_df, CO2_df)
upperBoundYear = r.upperYearBound(WaterCons_df, Temps_df, CO2_df)

WaterCons_df = WaterCons_df[(WaterCons_df['Year'] >= lowerBoundYear) & (WaterCons_df['Year'] <= upperBoundYear)].reset_index()
Temps_df = Temps_df[(Temps_df['Year'] >= lowerBoundYear) & (Temps_df['Year'] <= upperBoundYear)].reset_index()
CO2_df = CO2_df[(CO2_df['Year'] >= lowerBoundYear) & (CO2_df['Year'] <= upperBoundYear)].reset_index()

""" # Optional: graph of all 3 datasets
import matplotlib.pyplot as plt
waterVals = list(WaterCons_df['TotalCons'])
yVals = list(WaterCons_df['Year'])
tempVals = list(Temps_df['Temp'])
co2Vals = list(CO2_df['CO2'])
plt.plot(yVals, waterVals, yVals, tempVals, yVals, co2Vals)
plt.show() """

# Creating one dataframe to contain all of the data
TempsOnly_df = Temps_df['Temp']
CO2Only_df = CO2_df['CO2']
data = pd.concat([WaterCons_df, TempsOnly_df, CO2Only_df], axis=1, sort=False)
data = data.drop(columns=['index'])
print(data)

# 2: Finding highest and lowest ======================================================================
def printMyStats(year, water, temp, co2):
    print(' Year:', year)
    print('Water:', water)
    print(" Temp:", temp)
    print("  CO2:", co2)

# Find the water, temp and CO2 emissions given a year
def findYear(year, WaterCons_df, Temps_df, CO2_df):
    water = WaterCons_df[WaterCons_df['Year'] == year]
    water = water.iloc[0]['TotalCons']

    temp = Temps_df[Temps_df['Year'] == year]
    temp = temp.iloc[0]['Temp']

    co2 = CO2_df[CO2_df['Year'] == year]
    co2 = co2.iloc[0]['CO2']    

    data = {'water': water, 'temp': temp, 'co2': co2}
    return data

print("Lowest Water Consumption")
yearI = WaterCons_df['TotalCons'].idxmin()
year = WaterCons_df.loc[yearI]['Year']
dataForYear = findYear(year, WaterCons_df, Temps_df, CO2_df)
printMyStats(year, dataForYear['water'], dataForYear['temp'], dataForYear['co2'])

print("Highest Water Consumption")
yearI = WaterCons_df['TotalCons'].idxmax()
year = WaterCons_df.loc[yearI]['Year']
dataForYear = findYear(year, WaterCons_df, Temps_df, CO2_df)
printMyStats(year, dataForYear['water'], dataForYear['temp'], dataForYear['co2'])