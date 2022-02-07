import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("dataProject.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Brand"], show_hist="false")
fig.show()
