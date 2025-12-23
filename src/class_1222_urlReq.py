import urllib.request as req
import json
import pandas as pd

url = "https://api.gamer.com.tw/anime/v1/danmu.php?videoSn=45576&geo=TW%2CHK"
f = req.urlopen(url)
content = f.read()
content = json.loads(content)
danmus = content["data"]["danmu"]

# f = open("danmu.csv", "w", encoding="utf-8")
# f.write("userid,text\n")
# for i, d in enumerate(danmus):
#     duid = d["userid"]
#     dtext = d["text"]
#     if i < 5:
#         print(duid, dtext)
#     pat = '{},"{}"'
#     f.write(pat.format(duid, dtext) + "\n")
# f.close()

df = pd.DataFrame(danmus)
#index = False 可以把索引欄位去掉
df.to_csv("danmu.csv", encoding = "utf-8")
# df.to_excel("danmu.xlsx", index = False)