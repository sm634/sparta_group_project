import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


df = pd.read_csv('C:/Users/SMukhia/Desktop/Folder/Data/Medical insurance USA 2018.csv')
# print(df.head())

######## Cost of charges by Region ########

## First the number of patients admitted in the data for each region ##

regions_distinct = df['region'].unique()
print(regions_distinct)

# TRY!!
# users_northeast = df[df[df['region'] == 'northeast']]['charges'].mean()
# print(users_northeast)

users_northeast = df[df['region'] == 'northeast']
users_northwest = df[df['region'] == 'northwest']
users_southwest = df[df['region'] == 'southwest']
users_southeast = df[df['region'] == 'southeast']

n_users_northeast = np.size(users_northeast['charges'])
n_users_northwest = np.size(users_northwest['charges'])
n_users_southwest = np.size(users_southwest['charges'])
n_users_southeast = np.size(users_southeast['charges'])

print('Number of patients in northeast: ', n_users_northeast)
print('Number of patients in northwest: ', n_users_northwest)
print('Number of patients in southeast: ',n_users_southeast)
print('Number of patients in southwest: ', n_users_southwest)

####### Plotting a column graph of the number of users according to region #######

n_users_per_region = np.array([n_users_northeast, n_users_northwest, n_users_southeast, n_users_southwest])
region_names = np.array(['Northeast', 'Northwest', 'Southeast', 'SouthWest'])


###### Plotting the average charges incurred by region #####

avg_charges_northeast = users_northeast['charges'].mean().round()
avg_charges_northwest = users_northwest['charges'].mean().round()
avg_charges_southeast = users_southeast['charges'].mean().round()
avg_charges_southwest = users_southwest['charges'].mean().round()

avg_charges_by_region = np.array([avg_charges_northeast, avg_charges_northwest, avg_charges_southeast, avg_charges_southwest])

### The Bar chart ##

fig1, ax = plt.subplots(nrows=1, ncols=2)
ax[0].bar(region_names, n_users_per_region)
ax[0].set_xlabel('Region')
ax[0].set_ylabel('Number of Patients')
ax[0].set_title("The Number of Patients incurring Medical Insurance Charges by Region")

ax[1].barh(region_names, avg_charges_by_region)
ax[1].set_xlabel('Region')
ax[1].set_ylabel('Charges ($)')
ax[1].set_title("The Average Charges by Region ")

plt.show()






