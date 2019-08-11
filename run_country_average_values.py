from get_avg_values_function import *

path = 'C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/data.xlsx'
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

gdp = get_avg_per_country(path,sheet1)
rnd = get_avg_per_country(path,sheet2)
lf = get_avg_per_country(path,sheet3)
population = get_avg_per_country(path,sheet4)
energy = get_avg_per_country(path,sheet5)
unemployment = get_avg_per_country(path,sheet6)
employment = get_avg_per_country(path,sheet7)
migration = get_avg_per_country(path,sheet8)
trade = get_avg_per_country(path,sheet9)
tourism = get_avg_per_country(path,sheet10)
exchange_rate = get_avg_per_country(path,sheet11)


d1 = pd.merge(gdp,rnd,how='inner',left_on=gdp['Country Name'],right_on=rnd['Country Name'])
d2 = pd.merge(d1,lf,how='inner',left_on=d1['key_0'],right_on=lf['Country Name'])
d3 = pd.merge(d2,population,how='inner',left_on=d2['key_0'],right_on=population['Country Name'])
d4 = pd.merge(d3,energy,how='inner',left_on=d3['key_0'],right_on=energy['Country Name'])
d5 = pd.merge(d4,unemployment,how='inner',left_on=d4['key_0'],right_on=unemployment['Country Name'])
d6 = pd.merge(d5,employment,how='inner',left_on=d5['key_0'],right_on=employment['Country Name'])
d7 = pd.merge(d6,migration,how='inner',left_on=d6['key_0'],right_on=migration['Country Name'])
d8 = pd.merge(d7,trade,how='inner',left_on=d7['key_0'],right_on=trade['Country Name'])
d9 = pd.merge(d8,tourism,how='inner',left_on=d8['key_0'],right_on=tourism['Country Name'])
d10 = pd.merge(d9,exchange_rate,how='inner',left_on=d9['key_0'],right_on=exchange_rate['Country Name'])

print(d10)
d10.to_csv('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/to_regression_lf.csv')
