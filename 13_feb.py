# -*- coding: utf-8 -*-
"""13_feb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mpN73kJkVR3fTMsdru8NiwRjbOKlSla8

1.1: Read Total profit of all months and show it using a
line plot
Total profit data provided for each month. Generated line plot must include the following
properties:
● X label name = Month Number
● Y label name = Total profit

The line plot graph should look like this:
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/company_sales_data.csv")
df.head()

import numpy as np
x = df["month_number"]
y = df["total_profit"]

plt.plot(x, y)
plt.yticks(np.arange(100000, 600000, 100000))
plt.xticks(np.arange(1,13, 1))
plt.xlabel("Month Number")
plt.ylabel("Profit in Dollar")
plt.title("Company Profit Per month")



"""2: Get total profit of all months and show line plot with
the following Style properties
Generated line plot must include following Style properties:
● Line Style dotted and Line-color should be red
● Show legend at the lower right location.
● X label name = Month Number
● Y label name = Sold units number
● Add a circle marker.
● Line marker color as read
● Line width should be 3

The line plot graph should look like this:
"""

x=df["month_number"]
y=df["total_profit"]
plt.plot(x,y,"o--r",mfc="k",label="profit data of last year")
plt.xticks(np.arange(1,13, 1))
plt.xlabel("Month number")
plt.ylabel("profit in dollar")
plt.title("Company profit per month")
plt.legend(loc="lower right")



"""3.Read all product sales data and show it using a multiline plot Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ). The graph should look like this:"""

import numpy as np
x=df["month_number"]
plt.xticks(df["month_number"][::1])
plt.yticks(np.array([1000,2000,4000,6000,8000,10000,12000,15000,18000]))
y=df.facecream
z=df.facewash
y1=df.toothpaste
z1=df.bathingsoap
y2=df.shampoo
z2=df.moisturizer
plt.plot(x,y,marker="o",color = 'blue',label="facecream salesdata")
plt.plot(x,z,marker="o",color = 'orange',label="facewash salesdata")
plt.plot(x,y1,marker="o",color = 'green',label="toothpaste salesdata")
plt.plot(x,y2,marker="o",color = 'purple',label="bathingsoap salesdata")
plt.plot(x,z2,marker="o",color = 'brown',label="shampoo salesdata")
plt.plot(x,z1,marker="o",color = 'red',label="moisturizer salesdata")
plt.title("sales data")
plt.xlabel("month number")
plt.yticks(np.arange(1000,16000, 2000))
plt.ylabel("sales units in number")
plt.legend()

"""4.Read toothpaste sales data of each month and show it using a scatter plot Also, add a grid in the plot. gridline style should –.

The scatter plot should look like this
"""

plt.scatter(x,y1,label="tooth paste salesdata")
plt.xticks(df["month_number"][::1])
plt.grid()
plt.title("tooth paste sales data")
plt.xlabel("month number")
plt.ylabel("number of unit sold")
plt.legend()



"""5.Read face cream and facewash product sales data and show it using the bar chart The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart. The bar chart should look like this:"""

import matplotlib.pyplot as plt
import numpy as np

bar_width = 0.35
index = np.arange(len(df.month_number))

plt.bar(index, df.facecream, bar_width, label='Face Cream')
plt.bar(index + bar_width, df.facewash, bar_width, label='Facewash')
plt.xticks(index + bar_width / 2, df["month_number"])

plt.grid()
plt.title("Facewash and Facecream Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Number of Units Sold")
plt.legend(loc="upper left")
plt.show()



""" 6.Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk The bar chart should look like this:"""

plt.bar(x,df.bathingsoap)
plt.xticks(df.month_number[::1])
plt.xlabel("month number")
plt.ylabel("sales unit in number")
plt.title("bathing soap sales data")
plt.grid()



"""7.Read the total profit of each month and show it using the histogram to see the most common profit ranges The histogram should look like this:

"""

profitList = df ['total_profit'].tolist()
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label = 'Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Profit data')
plt.show()



"""8.Calculate total sale data for last year for each product and show it using a Pie chart Note: In Pie chart display Number of units sold per year for each product in percentage."""

totalsale=[df.facewash.sum(),df.facecream.sum(),df.toothpaste.sum(),df.bathingsoap.sum(),df.shampoo.sum(),df.moisturizer.sum()]
print(totalsale)
labels=["facewash","facecream","toothpaste","bathingsoap","shampoo","moisturizer"]
plt.pie(totalsale,labels=labels,autopct="%0.1f%%",)
plt.legend(loc="lower right")



"""9: Read Bathing soap facewash of all months and display it using the Subplot"""

monthlist=df.month_number.tolist()
bathsoap=df.bathingsoap.tolist()
facewash=df.facewash.tolist()
f,axarr = plt.subplots(2, sharex=True)
axarr[0].plot(monthlist, bathsoap, label = 'Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
axarr[0].set_title('Sales data of  a Bathingsoap')
axarr[1].plot(monthlist, facewash, label = 'Face Wash Sales Data', color='r', marker='o', linewidth=3)
axarr[1].set_title('Sales data of  a facewash')

plt.xticks(monthlist)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')



"""10: Read all product sales data and show it using the stack plot ."""

import matplotlib.pyplot as plt
x = df["month_number"]
y = df.facecream
z = df.facewash
y1 = df.toothpaste
z1 = df.bathingsoap
y2 = df.shampoo
z2 = df.moisturizer
plt.stackplot(x, y, z, y1, z1, y2, z2,
              labels=['Facecream', 'Facewash', 'Toothpaste', 'Bathingsoap', 'Shampoo', 'Moisturizer'],
              colors=['blue', 'orange', 'green', 'red', 'purple', 'brown'])

plt.title("Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Sales Units in Number")
plt.legend(loc='upper left')

plt.show()

