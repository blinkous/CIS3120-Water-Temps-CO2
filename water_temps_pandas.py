import pandas as pd
import my_reading_data as r
import my_create_web_page as w

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
# plt.show()
plt.savefig('blinkous.png') """

# Creating one dataframe to contain all of the data
TempsOnly_df = Temps_df['Temp']
CO2Only_df = CO2_df['CO2']
data = pd.concat([WaterCons_df, TempsOnly_df, CO2Only_df], axis=1, sort=False)
data = data.drop(columns=['index'])
print(data)

# 2: Finding highest and lowest ======================================================================
def getMyStatsPython(year, water, temp, co2):
    stats = """
 Year: """ + to_str(year) + """
Water: """ + to_str(water) + """
 Temp: """ + to_str(temp) + """
  CO2: """ + to_str(co2)
    return stats

def getMyStatsHTML(year, water, temp, co2):
    stats = w.myCreateNewTag("p", 'Year: ' + to_str(year))
    stats += """
""" + w.myCreateNewTag("p", 'Water: ' +to_str(water))
    stats += """
""" + w.myCreateNewTag("p", 'Temp: ' +to_str(temp))
    stats += """
""" + w.myCreateNewTag("p", 'CO2: ' +to_str(co2))
    return stats

def to_str(var):
    import numpy as np
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

def PrintMyStats(year, water, temp, co2):
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


stats = w.myCreateNewTag('h5','Lowest Water Consumption') + """
"""
yearI = WaterCons_df['TotalCons'].idxmin()
year = WaterCons_df.loc[yearI]['Year']
dataForYear = findYear(year, WaterCons_df, Temps_df, CO2_df)
stats += getMyStatsHTML(year, dataForYear['water'], dataForYear['temp'], dataForYear['co2'])

print()
yearI = WaterCons_df['TotalCons'].idxmax()
year = WaterCons_df.loc[yearI]['Year']
dataForYear = findYear(year, WaterCons_df, Temps_df, CO2_df)
stats += """
""" + w.myCreateNewTag('h5','Lowest Water Consumption') + """
""" + getMyStatsHTML(year, dataForYear['water'], dataForYear['temp'], dataForYear['co2'])

print(stats)

filename = 'file:///Users/Sara/Documents/Python/Group_Project/web_version/python_page.html'

w.createHtml(stats, filename)