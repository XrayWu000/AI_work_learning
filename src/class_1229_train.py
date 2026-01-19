import pandas as pd
import json5 as json
import ast


def extract_station_names(s):
    if pd.isna(s):
        return ""

    stations = ast.literal_eval(s)   # ← 關鍵修改

    pattern = ""
    for state in stations:
        if state.get("Show"):
            pattern += f"{state['StationName']}({state['DepartureTime']})/"

    return pattern

def func(s):
    return "桃園" in s

df = pd.read_csv("trains.csv", encoding="utf-8")
# 變成南港(06:05)/桃園(06:33)/台中(07:50)....

df["Stop_Station"] = df["StationInfo"].apply(extract_station_names)
df = df.drop("StationInfo", axis=1)
# 要有停桃園的
# 方法一
# cf = df[df["Stop_Station"].str.contains("桃園", na=False)]
# 方法二
cf = df[df["Stop_Station"].apply(func)]


print(cf[["TrainNumber", "Stop_Station"]].head())