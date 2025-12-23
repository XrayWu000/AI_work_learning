import urllib.request as req
import urllib.parse as par
import json
import pandas as pd
import datetime as dt

#GET是所有資料都在網址中
#POST某些參數被隱藏了，在payload中

stops = [
    "NanGang",
    "TaiPei",
    "BanQiao",
    "TaoYuan",
    "HsinChu",
    "MiaoLi",
    "TaiChung",
    "ChangHua",
    "YunLin",
    "ChiaYi",
    "Tainan",
    "ZuoYing"
]

hint = ""
for i in range(len(stops)):
    hint = hint + "[{}] {}\n".format(i, stops[i])

print("請選出發：")
start_stop_idx = int(input(hint))

print("請選到達：")
end_stop_idx = int(input(hint))


url = "https://www.thsrc.com.tw/TimeTable/Search"
data = {
    "SearchType": "S",
    "Lang": "TW",
    "StartStation": stops[start_stop_idx],
    "EndStation": stops[end_stop_idx],
    "OutWardSearchDate": "{}".format(dt.date.today().strftime("%Y/%m/%d")),
    "OutWardSearchTime": "00:00",
    "ReturnSearchDate": "{}".format(dt.date.today().strftime("%Y/%m/%d")),
    "ReturnSearchTime": "00:00",
    "DiscountType": ""
}
encode_data = par.urlencode(data).encode("utf-8")
f = req.urlopen(url, encode_data)
content = f.read()
content = json.loads(content)
trains = content["data"]["DepartureTable"]["TrainItem"]

df = pd.DataFrame(trains)
#index = False 可以把索引欄位去掉
df.to_csv("trains.csv", index = False, encoding = "utf-8")
# df.to_excel("trains.xlsx", index = False)