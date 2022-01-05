import pandas as pd

data = pd.read_csv("228_2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

df = pd.DataFrame(data["Primary Fur Color"].value_counts())
df.columns = ["Count"]
df.to_csv("squirrel.csv", index_label="Squirrel Color")
