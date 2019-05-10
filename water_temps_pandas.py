import pandas as pd
import my_reading_data as r
import my_create_web_page as w

# Initializing myHTMLContent to empty string, this will hold all of the content from this script that will be added to the webpage
myHTMLContent = ""

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

myHTMLContent += w.myCreateNewTagID('h3', 'Time Series Graphs', 'timeSeries')
# Graph of all 3 datasets
import matplotlib.pyplot as plt
waterVals = list(WaterCons_df['TotalCons'])
yVals = list(WaterCons_df['Year'])
tempVals = list(Temps_df['Temp'])
co2Vals = list(CO2_df['CO2'])
# plt.plot(yVals, waterVals, yVals, tempVals, yVals, co2Vals)
plt.clf()
myImages = ""
plt.plot(yVals, waterVals, color='skyblue')
plt.title("Water Consumption")
plt.savefig('water_graph.png')
myImages += w.myCreateImgTagClass('water_graph.png', 'graph')
plt.clf()

plt.plot(yVals, tempVals, color='green')
plt.title("Temperatures")
plt.savefig('temp_graph.png')
myImages += w.myCreateImgTagClass('temp_graph.png', 'graph')
plt.clf()

plt.plot(yVals, co2Vals, color='brown')
plt.title("CO2")
plt.savefig('co2_graph.png')
myImages += w.myCreateImgTagClass('co2_graph.png', 'graph')
plt.clf()

myHTMLContent += myImages

# Creating one dataframe to contain all of the data
TempsOnly_df = Temps_df['Temp']
CO2Only_df = CO2_df['CO2']
data = pd.concat([WaterCons_df, TempsOnly_df, CO2Only_df], axis=1, sort=False)
data = data.drop(columns=['index'])
# print(data)

# 2: Finding highest and lowest ======================================================================
# Get the stats in HTML form
def getMyStatsHTML(headTitle, year, water, temp, co2, myClass):
    stats = w.myCreateNewTag('h5',headTitle) + """
    """
    stats += w.myCreateNewTag("p", 'Year: ' + to_str(year))
    stats += """
    """ + w.myCreateNewTag("p", 'Water: ' +to_str(water))
    stats += """
    """ + w.myCreateNewTag("p", 'Temp: ' +to_str(temp))
    stats += """
    """ + w.myCreateNewTag("p", 'CO2: ' +to_str(co2))
    totalContent = w.myCreateNewTagClass("div", stats, myClass)
    return totalContent

def to_str(var):
    import numpy as np
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

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


def findMinMax(myData, myDataColumn, myMeasure, WaterCons_df, Temps_df, CO2_df, myhtmlContentFun, myClasses):
    # Getting the min
    yearI = myData[myDataColumn].idxmin()
    year = myData.loc[yearI]['Year']
    dataForYear = findYear(year, WaterCons_df, Temps_df, CO2_df)
    myhtmlContentFun += getMyStatsHTML("Lowest " + myMeasure, year, dataForYear['water'], dataForYear['temp'], dataForYear['co2'], myClasses)
    # Getting the max
    yearI = myData[myDataColumn].idxmax()
    year = myData.loc[yearI]['Year']
    dataForYear = findYear(year, WaterCons_df, Temps_df, CO2_df)
    myhtmlContentFun += getMyStatsHTML("Highest " + myMeasure, year, dataForYear['water'], dataForYear['temp'], dataForYear['co2'], myClasses)

    return myhtmlContentFun

# Getting max and mins
myHTMLContent += w.myCreateNewTagID('h3', 'Time Series Stats', 'timeSeriesStats')
myHTMLContent = findMinMax(WaterCons_df, 'TotalCons', 'Water Consumption', WaterCons_df, Temps_df, CO2_df, myHTMLContent, 'WaterStat')
myHTMLContent = findMinMax(Temps_df, 'Temp', 'Temperatures', WaterCons_df, Temps_df, CO2_df, myHTMLContent, 'TempStat')
myHTMLContent = findMinMax(CO2_df, 'CO2', 'CO2', WaterCons_df, Temps_df, CO2_df, myHTMLContent, 'CO2Stat')


filename = 'file:///Users/Sara/Documents/Python/Group_Project/web_version/python_page.html'

w.createHtml(myHTMLContent, filename)