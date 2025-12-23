import urllib.request as req
# beautifulsoup
import bs4 as bs
import pandas as pd

# 準備一個空的list
tabel = []

for i in range(20):
    page = i + 1
    url = f"https://tabelog.com/tw/tokyo/rstLst/sweets/{page}/?SrtT=rt"
    resp = req.urlopen(url)
    content = resp.read()
    html = bs.BeautifulSoup(content, "html.parser")
    # 區塊.find find_all
    # target = html.find("a", {"class": "list-rst__rst-name-target"})
    # # 特殊屬性: ["href"]
    # #內容: .get_text()
    # print(target["href"])
    # print(target.get_text())

    # targets是個list
    targets = html.find_all("div", {"class": "list-rst__body"})
    for t in targets:
        name = t.find("a", {"class": "list-rst__rst-name-target"})
        name_href = name["href"]
        name_text = name.get_text()

        rating = t.find("span", {"class": "c-rating__val"})
        rating_text = rating.get_text()

        place = t.find("div", {"class": "list-rst__area-genre"})
        place_text = place.get_text().strip()

        items = t.find_all("li", class_="list-rst__info-item")
        price_dict = {}
        for item in items:
            span = item.find("span", class_="c-rating-v3__val")
            if span is None:
                continue
            label = item.find("i")["aria-label"]      # 午餐預算 / 晚餐預算
            price = span.get_text().strip()
            price_dict[label] = price

        rest = t.find("span", {"class": "list-rst__holiday-text"})
        rest_text = rest.get_text().strip()
        print(name_text, name_href)
        print(rating_text, place_text, price_dict.get("晚餐預算"), price_dict.get("午餐預算"))
        print(rest_text)
        print("*" * 80)
        # 準備一筆資料
        row = {
            "rating": rating_text,
            "name": name_text,
            "url": name_href,
            "area_genre": place_text,
            "dinner_price": price_dict.get("晚餐預算"),
            "lunch_price": price_dict.get("午餐預算"),
            "holiday": rest_text
        }
        tabel.append(row)

#轉乘dataframe存檔
pd.DataFrame(tabel).to_csv("tablelog.csv", encoding = "utf-8")