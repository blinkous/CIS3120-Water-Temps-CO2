import pandas as pd

# 1: Reading the data in dataframes ======================================================================
# WATER CONSUMPTION
def readWater():
    # Read the file into Pandas Dataframe
    # WaterCons_df = pd.read_csv('Water_Consumption_In_The_New_York_City.csv')
    WaterCons_df = pd.read_csv('https://github.com/Razua9617/CIS3120/blob/master/daily_nyc_temp_data_1979_2017.csv')

    # Rename Columns so that it's easier to work with: TotalCons = total water consumption, CapitaCons = per capita water consumption
    WaterCons_df.columns = ['Year', 'Pop', 'TotalCons', 'CapitaCons']

    # Sort the Water Consumption dataframe by year
    WaterCons_df = WaterCons_df.sort_values(by=['Year'])
    return WaterCons_df

# TEMPERATURES
def readTemp():
    # Read the file into Pandas Dataframe, skip the first few rows with no data and drop rows with incomplete data
    # Temps_df = pd.read_csv('monthlyannualtempcentralpark.csv', skiprows=4)
    Temps_df = pd.read_csv('https://github.com/Razua9617/CIS3120/blob/master/monthlyannualtempcentralpark.csv', skiprows=4)
    Temps_df = Temps_df.dropna()

    # Take only the columns we want
    Temps_df = Temps_df[['YEAR','ANNUAL']]
    Temps_df = Temps_df[Temps_df['YEAR'] != 'YEAR'] # Cleaning the data, get rid of rows that start with Year

    # Rename Columns
    Temps_df.columns = ['Year', 'Temp']
    # Force conversion of data to numbers
    cols = Temps_df.columns
    Temps_df[cols] = Temps_df[cols].apply(pd.to_numeric, errors='coerce')
    return Temps_df

# CO2 EMISSIONS in case we still want this data
def readCO2():
    # Read the file into Pandas Dataframe, skip the first few rows with no data and drop rows with incomplete data
    # CO2_df = pd.read_csv('new_york_co2_emissions.csv', skiprows=3)
    CO2_df = pd.read_csv('https://github.com/Razua9617/CIS3120/blob/master/new_york_co2_emissions.csv', skiprows=3)

    # Drop the first column
    CO2_df.drop(CO2_df.columns[0], axis=1, inplace=True)
    # Rename column
    CO2_df.rename(columns = {list(CO2_df)[0]: 'C02'}, inplace = True)

    # Grab only the data from the CO2 totals
    CO2_df = CO2_df[CO2_df['C02'] == 'Grand Total']

    # Switch the columns and rows
    CO2_df = CO2_df.T
    CO2_df = CO2_df.reset_index()

    CO2_df.columns = ['Year', 'CO2']
    CO2_df = CO2_df.iloc[1:] # Remove the first row because it only has the original header values
    # Force conversion of data to numbers
    cols = CO2_df.columns
    CO2_df[cols] = CO2_df[cols].apply(pd.to_numeric, errors='coerce')
    return CO2_df

# Find lower bound for years range
def lowerYearBound(WaterCons_df, Temps_df, CO2_df):
    lowerBoundYears = []
    lowerBoundYears.append(WaterCons_df['Year'].min())
    lowerBoundYears.append(Temps_df['Year'].min())
    lowerBoundYears.append(CO2_df['Year'].min())
    lowerBoundYear = max(lowerBoundYears)
    return lowerBoundYear

# Find lower bound for years range
def upperYearBound(WaterCons_df, Temps_df, CO2_df):
    upperBoundYears = []
    upperBoundYears.append(WaterCons_df['Year'].max())
    upperBoundYears.append(Temps_df['Year'].max())
    upperBoundYears.append(CO2_df['Year'].max())
    upperBoundYear = min(upperBoundYears)
    return upperBoundYear