import numpy as np
import pandas as pd
from get_avg_values_function import *

path = 'C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/data_year.xlsx'
sheet1='gdp'
sheet2='R&D'
sheet3='labour_force'
sheet4='population'
sheet5='energy_consumption'
sheet6='unemployment'
sheet7='employment'
sheet8='net_migration'
sheet9='trade'
sheet10='tourism'
sheet11='exchange_rate'

# df = pd.read_excel(path,sheet1)
# df = df.fillna(0)
# df = df.transpose()
# years = df.index
# years = pd.DataFrame(years)
# values = df.values[1:, :]
# values_array = np.array(values)

gdp = get_avg_per_year(path,sheet1)
rnd = get_avg_per_year(path,sheet2)
lf = get_avg_per_year(path,sheet3)
population = get_avg_per_year(path,sheet4)
energy = get_avg_per_year(path,sheet5)
unemployment = get_avg_per_year(path,sheet6)
employment = get_avg_per_year(path,sheet7)
migration = get_avg_per_year(path,sheet8)
trade = get_avg_per_year(path,sheet9)
tourism = get_avg_per_year(path,sheet10)
exchange_rate = get_avg_per_year(path,sheet11)

d1 = pd.merge(gdp,rnd,how='inner',left_on=gdp['0_x'],right_on=rnd['0_x'])
d2 = pd.merge(d1,lf,how='inner',left_on=d1['key_0'],right_on=lf['0_x'])
d3 = pd.merge(d2,population,how='inner',left_on=d2['key_0'],right_on=population['0_x'])
d4 = pd.merge(d3,energy,how='outer',left_on=d3['key_0'],right_on=energy['0_x'])
d5 = pd.merge(d4,unemployment,how='outer',left_on=d4['key_0'],right_on=unemployment['0_x'])
d6 = pd.merge(d5,employment,how='outer',left_on=d5['key_0'],right_on=employment['0_x'])
d7 = pd.merge(d6,migration,how='outer',left_on=d6['key_0'],right_on=migration['0_x'])
d8 = pd.merge(d7,trade,how='outer',left_on=d7['key_0'],right_on=trade['0_x'])
d9 = pd.merge(d8,tourism,how='outer',left_on=d8['key_0'],right_on=tourism['0_x'])
d10 = pd.merge(d9,exchange_rate,how='outer',left_on=d9['key_0'],right_on=exchange_rate['0_x'])

# print(d10)

d10.to_csv('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/to_regression_year.csv')
