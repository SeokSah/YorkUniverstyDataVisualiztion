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

majorData = data[["SumOfftbk hds","Major1 ", "Faculty", "Gender", "QF Year", "FT / PT"]]

majorData.drop(data.loc[data['Major1 '] == "Other / Specials"].index, inplace=True)
majorData = majorData[majorData["Gender"] != "Not Reported"]
majorData.dropna(inplace=True)


majorEngineerData = majorData[majorData["Faculty"] == "Lassonde School of Engineering"]
majorData = majorData[majorData["Faculty"] == "Faculty of Science"]

majorData = majorData.sort_values(["Faculty"])
majorEngineerData = majorEngineerData.sort_values(["Faculty"])


#Group by major, year, and gender then sum them up
yearlyMajor = majorData.groupby(["QF Year",'Major1 ', "Gender"], as_index= False).sum()
yearlyEngineerMajor = majorEngineerData.groupby(["QF Year",'Major1 ', "Gender"], as_index= False).sum()

#Create a subplot and set its size for the plots of majors by each year
fig, axs = plt.subplots(1,2)
fig.set_size_inches(18, 7)

#Generate plots
def generate_plot(row, column, faculty, year, data):
    plot = sns.barplot(x = "Major1 ", y = "SumOfftbk hds", data= data[data["QF Year"] == year], ax=axs[row], hue="Gender")
    plot.set_xticklabels(plot.get_xticklabels(), rotation=40, ha="right")
    #data[data["QF Year"] == year]["Major1 "] this may be needed to replace get xticklabels for special cases
    plot.set(xlabel = "", ylabel="", title="Number of Students in the " + faculty + " by Major in " + year)
    return plot

def plot_text(plot):
    for p in plot.patches:
             plot.annotate("%.0f" % p.get_height(), (p.get_x() + p.get_width() / 2, p.get_height()),
                 ha='center', va='center', fontsize=8, color='black', xytext=(0, 4),
                 textcoords='offset points')

plot1 = generate_plot(0, 0, "Faculty of Science", "2019-20", yearlyMajor)   
plot2 = generate_plot(1, 0, "Lassonde School of Engineering", "2019-20", yearlyEngineerMajor)                     
             
plot_text(plot1)
plot_text(plot2)

fig.tight_layout()
print(yearlyMajor.head)
