import urllib.request as req
import pandas as pd

df = pd.read_csv("danmu.csv", encoding = "utf-8", index_col = 0)
times = df["userid"].value_counts()
target = times[times < 20].head(1).index[0]
fil = df["userid"] == target
a = df[fil]
print(a)