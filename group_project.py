import numpy as np
import pandas as pd

##### Getting avg gdp ######
df = pd.read_excel('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/data.xlsx',sheet_name='gdp')

df = df.fillna(0)
countries = df['Country Name'] # Countries Df
gdp_values = df.iloc[:,1:]
gdp_array = np.array(gdp_values) # gdp array

avg_values_countries = [] # initiate list

for i in range(0,len(gdp_array[0:])):
    avg_gdp_per_country = gdp_array[i].mean()
    avg_values_countries.append(avg_gdp_per_country)

avg_gdp_array = np.array(avg_values_countries)
avg_gdp_df = pd.DataFrame(avg_gdp_array)
# combine dataframes
avg_data_gdp = pd.merge(countries,avg_gdp_df,how="inner",on=countries.index)

# avg_data_gdp.to_csv("C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/d1.csv")

##### Getting avg R&D #####

df1 = pd.read_excel('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/data.xlsx',sheet_name='R&D')

df1 = df1.fillna(0)
countries1 = df1['Country Name'] # Countries Df
rnd_values = df1.iloc[:,1:]
rnd_array = np.array(rnd_values) # gdp array

avg_rnd_countries = [] # initiate list

for i in range(0,len(rnd_array[0:])):
    avg_gdp_per_country = rnd_array[i].mean()
    avg_rnd_countries.append(avg_gdp_per_country)

avg_rnd_array = np.array(avg_rnd_countries)
avg_rnd_df = pd.DataFrame(avg_rnd_array)
# combine dataframes
avg_data_rnd = pd.merge(countries1,avg_rnd_df,how="inner",on=countries1.index)

# avg_data_rnd.to_csv('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/d2.csv')

##### Getting avg energy consumption #####

df2 = pd.read_excel('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/data.xlsx',sheet_name='energy_consumption')

df2 = df2.fillna(0)

countries2 = df2['Country Name'] # Countries Df
ec_values = df2.iloc[:,1:]
ec_array = np.array(ec_values) # gdp array

avg_ec_countries = [] # initiate list

for i in range(0,len(ec_array[0:])):
    avg_ec_per_country = ec_array[i].mean()
    avg_ec_countries.append(avg_ec_per_country)

avg_ec_array = np.array(avg_ec_countries)
avg_ec_df = pd.DataFrame(avg_ec_array)
# combine dataframes
avg_data_ec = pd.merge(countries2,avg_ec_df,how="inner",on=countries2.index)

# avg_data_ec.to_csv('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/d3.csv')
##### Getting avg unemployment #####

df3 = pd.read_excel('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/data.xlsx',sheet_name='unemployment')

df3 = df3.fillna(0)

countries3 = df3['Country Name'] # Countries Df
unemployment_values = df3.iloc[:,1:]
unemployment_array = np.array(unemployment_values) # gdp array

avg_unemployment_countries = [] # initiate list

for i in range(0,len(unemployment_array[0:])):
    avg_unemployment_per_country = unemployment_array[i].mean()
    avg_unemployment_countries.append(avg_unemployment_per_country)

avg_unemployment_array = np.array(avg_unemployment_countries)
avg_unemployment_df = pd.DataFrame(avg_unemployment_array)
# combine dataframes
avg_data_unemployment = pd.merge(countries3,avg_unemployment_df,how="inner",on=countries3.index)

# avg_data_unemployment.to_csv('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/d4.csv')

##### Getting avg employment #####

df4 = pd.read_excel('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/data.xlsx',sheet_name='employment')

df4 = df4.fillna(0)

countries4 = df4['Country Name'] # Countries Df
employment_values = df4.iloc[:,1:]
employment_array = np.array(employment_values) # gdp array

avg_employment_countries = [] # initiate list

for i in range(0,len(employment_array[0:])):
    avg_employment_per_country = employment_array[i].mean()
    avg_employment_countries.append(avg_employment_per_country)

avg_employment_array = np.array(avg_employment_countries)
avg_employment_df = pd.DataFrame(avg_employment_array)
# combine dataframes
avg_data_employment = pd.merge(countries4,avg_employment_df,how="inner",on=countries4.index)

# avg_data_employment.to_csv('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/d5.csv')
##### avg net migration #####

df5 = pd.read_excel('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/data.xlsx',sheet_name='net_migration')

df5 = df5.fillna(0)

countries5 = df5['Country Name'] # Countries Df
migration_values = df5.iloc[:,1:]
migration_array = np.array(migration_values) # gdp array

avg_migration_countries = [] # initiate list

for i in range(0,len(migration_array[0:])):
    avg_migration_per_country = migration_array[i].mean()
    avg_migration_countries.append(avg_migration_per_country)

avg_migration_array = np.array(avg_migration_countries)
avg_migration_df = pd.DataFrame(avg_migration_array)
# combine dataframes
avg_data_migration = pd.merge(countries5,avg_migration_df,how="inner",on=countries5.index)

# avg_data_migration.to_csv('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/d6.csv')
##### avg population data ######

df6 = pd.read_excel('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/data.xlsx',sheet_name='population')

df6 = df6.fillna(0)

countries6 = df6['Country Name'] # Countries Df
population_values = df6.iloc[:,1:]
population_array = np.array(population_values) # gdp array

avg_population_countries = [] # initiate list

for i in range(0,len(population_array[0:])):
    avg_population_per_country = population_array[i].mean()
    avg_population_countries.append(avg_population_per_country)

avg_population_array = np.array(avg_population_countries)
avg_population_df = pd.DataFrame(avg_population_array)
# combine dataframes
avg_data_population = pd.merge(countries6,avg_population_df,how="inner",on=countries6.index)

# avg_data_population.to_csv('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/d7.csv')



data1 = pd.merge(avg_data_gdp,avg_data_rnd,how="inner",left_on=avg_data_gdp['Country Name'],right_on=avg_data_rnd['Country Name'])
data2 = pd.merge(data1,avg_data_ec,how="inner",left_on=data1['Country Name_x'],right_on=avg_data_ec['Country Name'])
# print(data2)
data3 = pd.merge(data2,avg_data_employment,how="inner",left_on=data2['key_0'],right_on=avg_data_employment['Country Name'])
#print(data3)
data4 = pd.merge(data3,avg_data_unemployment,how="inner",left_on=data3['key_0'],right_on=avg_data_unemployment['Country Name'])
#print(data4)
data5 = pd.merge(data4,avg_data_migration,how="inner",left_on=data4['key_0'],right_on=avg_data_migration['Country Name'])
# print(data5)
data6 = pd.merge(data5,avg_data_population,how="inner",left_on=data5['key_0'],right_on=avg_data_population['Country Name'])
# print(data6)

data6.to_csv('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/for_regression.csv')
