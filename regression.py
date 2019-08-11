import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_excel('C:/Users/SMukhia/Desktop/weekly_work/week_5&6/Group work/python_cleaning/to_regression_year.xlsx',sheet_name='for regression')


y = df['gdp']
x = df.iloc[:,2:]

y = np.array(y)
x = np.array(x)
x = sm.add_constant(x)

# print(y)
# print(x)

model = sm.WLS(y,x)
results = model.fit()
to_write = results.summary()
print(to_write)

to_write = str(to_write)

file = open('results_year.txt','w')
file.write(to_write)
