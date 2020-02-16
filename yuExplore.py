#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:26:18 2020

@author: seoksah
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 500)

data = pd.read_csv("UG_Enrolment_Headcount_-_Table_data.csv")

print (data.columns)

majorData = data[["SumOfftbk hds","Major1 ", "Faculty", "Gender", "QF Year", "FT / PT"]]

majorData.drop(data.loc[data['Major1 '] == "Other / Specials"].index, inplace=True)
majorData = majorData[majorData["Faculty"] == "Faculty of Science"]
majorData = majorData[majorData["Gender"] != "Not Reported"]
majorData.dropna(inplace=True)

#majorData = majorData[majorData["Faculty"] == "Lassonde School of Engineering"]

#print(majorData.head())

majorData = majorData.sort_values(["Faculty"])


# =============================================================================
#                      Extra Exploratory Plot
# #plt.figure(figsize=(40,4))
# #plot = sns.countplot("Major1 ", data=majorData)
# #plot.set_xticklabels(plot.get_xticklabels(), rotation=40, ha="right")
# =============================================================================

#Group by major, year, and gender then sum them up
yearlyMajor = majorData.groupby(["QF Year",'Major1 ', "Gender"], as_index= False).sum()

#Create a subplot and set its size for the plots of majors by each year
fig, axs = plt.subplots(4,2)
fig.set_size_inches(22, 32)

#Generate plots
def generate_plot(row, column, year):
    plot = sns.barplot(x = "Major1 ", y = "SumOfftbk hds", data= yearlyMajor[yearlyMajor["QF Year"] == year], ax=axs[row, column], hue="Gender")
    plot.set_xticklabels(plot.get_xticklabels(), rotation=40, ha="right")
    #yearlyMajor[yearlyMajor["QF Year"] == year]["Major1 "] this may be needed to replace get xticklabels for special cases
    plot.set(xlabel = "", ylabel="", title="Number of Students in the Faculty of Science by Major in " + year)
    return plot

def plot_text(plot):
    for p in plot.patches:
             plot.annotate("%.0f" % p.get_height(), (p.get_x() + p.get_width() / 2, p.get_height()),
                 ha='center', va='center', fontsize=8, color='black', xytext=(0, 4),
                 textcoords='offset points')
             
plot1 = generate_plot(0, 0, "2012-13")
plot2 = generate_plot(0, 1, "2013-14")
plot3 = generate_plot(1, 0, "2014-15")
plot4 = generate_plot(1, 1, "2015-16")     
plot5 = generate_plot(2, 0, "2016-17") 
plot6 = generate_plot(2, 1, "2017-18")   
plot7 = generate_plot(3, 0, "2018-19")   
plot8 = generate_plot(3, 1, "2019-20")                     
             
plot_text(plot1)
plot_text(plot2)
plot_text(plot3)
plot_text(plot4)
plot_text(plot5)
plot_text(plot6)
plot_text(plot7)
plot_text(plot8)

fig.tight_layout()
print(yearlyMajor.head)
