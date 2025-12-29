import urllib.request as req
import pandas as pd
import re

def remove_jpy(n):
    n = n.replace("JPY ", "")
    if n == "":
        n = "-"
    return n

def split_area_genre(s):
    s_spl = s.split(" / ")
    if len(s_spl) == 1:
        area = "-"
        genre = s_spl[0]
    else:
        area = s_spl[0]
        genre = s_spl[1]
    ans = {"area": area, "genre": genre}
    return pd.Series(ans)

def split_price(s):
    ans = {"min_price": "-", "max_price": "-"}
    s_spl = re.split(r"\s*-\s*", s)
    ans["min_price"] = remove_jpy(s_spl[0])
    ans["max_price"] = remove_jpy(s_spl[1])
    return pd.Series(ans)

df = pd.read_csv("tabelog.csv", encoding="utf-8", index_col=0)
df[["area", "genre"]] = df["area_genre"].apply(split_area_genre)
df[["min_price_dinner", "max_price_dinner"]] = df["dinner_price"].apply(split_price)
cf = df[
    pd.to_numeric(
        df["max_price_dinner"].str.replace(",", "", regex=False),
        errors="coerce"
    ) < 10000
]

print(cf.head(7))