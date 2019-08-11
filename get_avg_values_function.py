import numpy as np
import pandas as pd

##### Getting avg for each country from excel data ######

path = 'C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/data.xlsx'
sheet_name='gdp'

def get_avg_per_country(file_path,sheet):
    df = pd.read_excel(file_path,sheet_name=sheet)
    df = df.fillna(0)
    countries = df['Country Name']
    values = df.iloc[:,1:]
    values_array = np.array(values)

    avg_values_countries = []

    for i in range(0,len(values_array[0:])):
        avg_value_per_country = values_array[i].mean()
        avg_values_countries.append(avg_value_per_country)

    avg_array = np.array(avg_values_countries)
    avg_df = pd.DataFrame(avg_array)
    # combine dataframes
    return pd.merge(countries,avg_df,how="inner",on=countries.index)


def get_avg_per_year(file_path,sheet):
    df = pd.read_excel(file_path,sheet_name=sheet)
    df = df.fillna(0)
    df = df.transpose()
    years = df.index
    years = pd.DataFrame(years)
    values = df.values[1:,:]
    values_array = np.array(values)
    avg_array = values_array.mean(1)

    # avg_values_year = []
    #
    # for i in range(0,len(values_array[0:])):
    #     each_value = []
    #     for j in range(0,len(values_array[0][0:])):
    #         if j != 0:
    #             each_value.append(j)
    #         avg_value_per_year = np.array(each_value).mean()
    #     avg_values_year.append(avg_value_per_year)
    #
    # avg_array = np.array(avg_values_year)
    avg_df = pd.DataFrame(avg_array)
    # combine dataframes
    return pd.merge(years,avg_df,how="inner",left_on=years.index,right_on=avg_df.index)

