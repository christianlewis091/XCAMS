"""
Jocelyn requested that I take a look at some of the recombusted blank.
This refers to:
14047/1 and 14047/11, and how the blanks look during normal scenarious versus "recombustion" scenarios.

Margaret will tell me the job# of the ones that have been recombusted.
14047/11: 221623, 221624, 221625
14047/1: 221248, 221626, 221627

"""
import pandas as pd
import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import seaborn as sns

def long_date_to_decimal_date(x):
    array = []  # define an empty array in which the data will be stored
    for i in range(0, len(x)):  # initialize the for loop to run the length of our dataset (x)
        j = x[i]  # assign j: grab the i'th value from our dataset (x)
        decy = pyasl.decimalYear(j)  # The heavy lifting is done via this Py-astronomy package
        decy = float(decy)  # change to a float - this may be required for appending data to the array
        array.append(decy)  # append it all together into a useful column of data
    return array  # return the new data

size1 = 5
colors = sns.color_palette("rocket", 6)
colors2 = sns.color_palette("mako", 6)
seshadri = ['#c3121e', '#0348a1', '#ffb01c', '#027608', '#0193b0', '#9c5300', '#949c01', '#7104b5']

bar_1 = pd.read_excel(r'C:\Users\clewis\IdeaProjects\GNS\XCAMS_data\bar1.xlsx')
bar_11 = pd.read_excel(r'C:\Users\clewis\IdeaProjects\GNS\XCAMS_data\bar11.xlsx')

bar_1 = bar_1.loc[(bar_1['R'] == '14047/1')]  # when exporting from RLIMS, asking for 14047/1 actually gave me 14047/1, /11, and /12.

bar_1 = bar_1.dropna(subset='Ratio to standard').reset_index(drop=True)  # clean up the file by dropping all the empty rows that come from the importation of the prepocessing data.
bar_11 = bar_11.dropna(subset='Ratio to standard').reset_index(drop=True)  # clean up the file by dropping all the empty rows that come from the importation of the prepocessing data.
x = bar_1['Date Run']
bar_1['Date Run'] = long_date_to_decimal_date(x)  # convert dates to decimal dates.
x = bar_11['Date Run']
bar_11['Date Run'] = long_date_to_decimal_date(x)
bar_1 = bar_1[['Date Run','Ratio to standard','Ratio to standard error','Job']]
bar_1.to_excel('bar1clean.xlsx')
bar_11 = bar_11[['Date Run','Ratio to standard','Ratio to standard error','Job']]
bar_11.to_excel('bar11clean.xlsx')
"""
This is the quick and dirty way to exclude the test samples from the normal background dataset, this probably could be
done with a nice list and loop, or a really nice pandas indexing function but need the quick result for now. 
"""
bar_1 = bar_1.loc[(bar_1['Ratio to standard'] < .009)]      # This line and the one below filters for outliers that could skew the final analysis.
bar_11 = bar_11.loc[(bar_11['Ratio to standard'] < .009)]

bar_1_a = bar_1.loc[(bar_1['Job'] != 221248.0)]
bar_1_a = bar_1_a.loc[(bar_1['Job'] != 221626.0)]
bar_1_a = bar_1_a.loc[(bar_1['Job'] != 221627.0)]

bar_11_a = bar_11.loc[(bar_11['Job'] != 221623.0)]
bar_11_a = bar_11_a.loc[(bar_11['Job'] != 221624.0)]
bar_11_a = bar_11_a.loc[(bar_11['Job'] != 221625.0)]

x = pd.DataFrame({})
y = pd.DataFrame({})
list1 = [221248.0, 221626.0, 221627.0]
list2 = [221623.0, 221624.0, 221625.0]

for i in range(0, len(list1)):
    k = bar_1.loc[(bar_1['Job'] == list1[i])]
    x = pd.concat([x, k])

for i in range(0, len(list2)):
    k = bar_1.loc[(bar_1['Job'] == list1[i])]
    y = pd.concat([y, k])

"""
What's the average and 1-sigma of the standards when I only look at the non-Recombusted ones (the normal ones?)
"""

bar_1_average = np.average(bar_1_a['Ratio to standard'])
bar_11_average = np.average(bar_11_a['Ratio to standard'])

bar_1_std = np.std(bar_1_a['Ratio to standard'])
bar_11_std = np.std(bar_11_a['Ratio to standard'])

bar_1_recombusted_average = np.average(x['Ratio to standard'])
bar_11_recombusted_average = np.average(y['Ratio to standard'])

bar_1_recombusted_std = np.std(x['Ratio to standard'])
bar_11_recombusted_std = np.std(y['Ratio to standard'])


print("The average RTS of 14047/1, normally is: {} \u00B1 {} ".format(bar_1_average, bar_1_std))
print("The average RTS of 14047/1, recombusted is: {} \u00B1 {} ".format(bar_1_recombusted_average, bar_1_recombusted_std))

print("The average RTS of 14047/11, normally is: {} \u00B1 {} ".format(bar_11_average, bar_11_std))
print("The average RTS of 14047/11, recombusted is: {} \u00B1 {} ".format(bar_11_recombusted_average, bar_11_recombusted_std))















# x = bar_1['Job']
# print(x[1])
#
# if x[1] == 112005.0:
#     print('yes')







