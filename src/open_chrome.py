import os
import time
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

# 如果你是MAC, 遇到SSL Certificate Failed: 就加這兩行
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 你要把你所有的平常動作模擬在這裡
if __name__ == '__main__':
    driver = uc.Chrome(use_subprocess=False)
    driver.get("https://www.google.com")
    driver.maximize_window()
    # bs:find/find_all
    # selenium:find_element/find_elements
    # TAG_NAME/CLASS_NAME/ID
    e = driver.find_element(By.CLASS_NAME, "gLFyf")
    # click() send_keys()
    e.send_keys("chiikawa")
    e.send_keys(Keys.ENTER)
    time.sleep(2)

    es = driver.find_elements(By.CLASS_NAME, "C6AK7c")
    es[2].click()
    time.sleep(2)

    dn = "chiilawa"
    if not os.path.exists(dn):
        os.makedirs(dn)
    es = driver.find_elements(By.TAG_NAME, "img")
    for e in es:
        e_src = e.get_attribute("src")
        if not e_src == None:
            fn = dn + "/" + str(time.time()) + ".png"
            req.urlretrieve(e_src, fn)

    # bs: ["href"]/get_text() .text
    # selenium: get_attributed("href")/.text

    time.sleep(3)
    # input("Press Enter to close browser...")

    driver.quit()