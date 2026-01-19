import urllib.request as req
import pandas as pd

# DepartureTime 9:00~12:00 ， Duration < 2hr
df = pd.read_csv("trains.csv", encoding = "utf-8", index_col = 0)
fil1 = (df["DepartureTime"] >= "09:00") & (df["DepartureTime"] <= "12:00")
fil2 = df["Duration"] < "02:00"
a = df[fil1 & fil2]
print(a[["Sequence", "DepartureTime", "Duration"]])