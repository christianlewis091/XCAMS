"""
Jocelyn requested that I take a look at some of the recombusted blank.
This refers to:
14047/1 and 14047/11, and how the blanks look during normal scenarious versus "recombustion" scenarios.

Margaret will tell me the job# of the ones that have been recombusted.
14047/1: 221623, 221624, 221625
14047/11: 221248, 221626, 221627

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
bar_1 = bar_1.loc[(bar_1['R'] == '14047/1')]
bar_11 = pd.read_excel(r'C:\Users\clewis\IdeaProjects\GNS\XCAMS_data\bar11.xlsx')
bar_1 = bar_1.dropna(subset='Ratio to standard').reset_index(drop=True)  # clean up the file by dropping all the empty rows that come from the importation of the prepocessing data.
bar_11 = bar_11.dropna(subset='Ratio to standard').reset_index(drop=True)  # clean up the file by dropping all the empty rows that come from the importation of the prepocessing data.
x = bar_1['Date Run']
bar_1['Date Run'] = long_date_to_decimal_date(x)

x = bar_11['Date Run']
bar_11['Date Run'] = long_date_to_decimal_date(x)




