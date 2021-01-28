# -*- coding: utf-8 -*-
"""COVID_Project_code.ipynb


**COVID 19 Project** .

Full Analysis.

Top Class Project !

By- SHIVAM VATSHAYAN

vatshayan007@gmail.*com*
"""

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
df.head()

df.columns

df.describe

df.shape

df.size

import seaborn as sns

sns.scatterplot (x="cases", y="deaths", 
                hue="deaths",size="deaths", data=df)

"""WAIT WAIT WAIT !!

Project is longer and It is Only Demo.

For Full Project Code, Mail me at vatshayan007@gmail.com Now.

Project is very Interesting and Easy to Understand

I will send you PPT, Report and Project code directly.

Mail me Now **vatshayan007@gmail.com** for Full Project !

Let's Learn, work and Grow together.
Ask freely!
"""



