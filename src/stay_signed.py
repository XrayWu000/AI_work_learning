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
# cookie: 你做完第一次，伺服器要求你設置一組通關密碼，
if __name__ == '__main__':
    driver = uc.Chrome(use_subprocess=False)
    driver.get("https://www.google.com")
    driver.maximize_window()

    str_cookie = "AEC=AaJma5tT7DEF6_T0wapD11fFEdrtOY9bqJ7wpvPL0IVyrJi-fyR3TtpLLg; __Secure-BUCKET=COgD; __Secure-STRP=AD6Dogup5U1nOh8Qaw5YyF0YhKhaAbvrF4NWwYe6awLiW9v8WYdjTooLP0a_QqTa0f1o9BBVkPqX1E7xzJi33KELdm0vpwO4u1CP; OTZ=8431692_24_24__24_; NID=528=YWSoUg3jJKe-h-RwTeWagQ6bms02OV_DXJBYlSiZ0d3UiGKtVBro2ZlDILjlMNoq7Uqd9gVBTTvY1BvLPyEhwZoLh5Ai4GpQZ18I_4W18tA5WHHzGJqONKESwGEAvzFFJj9R8Qu1b4awC2SFMU_ieN68v-EeXYN5c5Jul5aG2lALIOAhq3uJdXFalY3duutHuoudjZE-eipYo4T9GI4gx4EfBB6Rk1mfGUQGrk5Uypuj6p8byDjRJduU0OBQic97BEf8Z6-FkyYWwLuOKmw37f-c9jdLfVo4bxqKV_A1o9Yww2CsAkHR_EdUeZjg_4vu7SCjwbox3f77EVYj7nV4FKSKw4uaHNRLks83IdRWbq2-AAnqvWD4hyDaJJ5azYU4AhK_MGjVGZAixe-hWbuobfhixok3nhuEhPOcuAz21I5cYHDU0282dV_tmNYSTHRISt3sWkzxYdi61XIDLpua42SSrOoZpraxfCn2f8QEc_WSa0hDS-nc21kar9O-EHwhH_nrsgntipkMKydXLJWLD-bH67FnlaO5KPHogQ_OfhigLFP5dG3h8wmfBqf6JgOA8wWHMHU2qc7XtxE_9TvD6qVFCoCnQUbnjdsId1OkqBGiVRIaYknsLZoRRefF3j-_WS3YI7q-C3mAYsO8dF3DHUDHMgjUo73C7D2RBoP90s07ySvFPxAxLe2kXc3Tq3rjIAvK0VM50cF_hbQwuzaxRHZ-TRbIc0ya56xhHFjP_gs; SID=g.a0005ghS9457d0ZkZ3DCkXzSPW_Pbh0bWIXDOUHL_VIA23HXjTBWhxBJc52sg35h7pHmKqT5HwACgYKAeQSARISFQHGX2MiGSvhG2Xc0O900xU0OoHkBhoVAUF8yKrMZD8rR4QfeFx8LuCXvRKU0076; __Secure-1PSID=g.a0005ghS9457d0ZkZ3DCkXzSPW_Pbh0bWIXDOUHL_VIA23HXjTBW-Bcay4um_W144ahCIggNDQACgYKAfcSARISFQHGX2Miet1EOgEB8HkMXT-cxB-Z6xoVAUF8yKrk90ow30Iyu_DX1C3LwIUI0076; __Secure-3PSID=g.a0005ghS9457d0ZkZ3DCkXzSPW_Pbh0bWIXDOUHL_VIA23HXjTBW3jQoq7AzElkQ9EGt7mkIvwACgYKAS0SARISFQHGX2Mieu6kvX1jronwN9Xv22XzkxoVAUF8yKq6KaEnt-SpalHsqrR4S7Wc0076; LSID=g.a0005ghS98oaezAk520sVUpNyfikF2S0ZRjITguy8_-94qPmoOwuabyuF9isHoQRUkKaoZYN0gACgYKARoSARISFQHGX2MiO8T2ecqeC6sF6i6eLKCJNRoVAUF8yKqydkaJXZvx9xuUhV9LkqiH0076; __Host-1PLSID=g.a0005ghS98oaezAk520sVUpNyfikF2S0ZRjITguy8_-94qPmoOwuQRoy3G1RX6Hkj2cMQ9I_VAACgYKAbkSARISFQHGX2Mi6hh8YHDHpKowZDTrUT82IhoVAUF8yKpIvtHHjaXUujBezMOedxgK0076; __Host-3PLSID=g.a0005ghS98oaezAk520sVUpNyfikF2S0ZRjITguy8_-94qPmoOwucluOxfP3o-5c4bjqAM1PHgACgYKARwSARISFQHGX2Mifu0j9qbofr9sm3HNzfiOZxoVAUF8yKrcQxtH2a2EMHgKUhxzODKq0076; HSID=AuXUEmx3-9YWjUkT1; SSID=AWxX0k0PRhxR95-RD; APISID=YfmRoclMwHrbsTK7/ADttp69MegJMD5B4c; SAPISID=MsqFPyKNSnLA6qpF/AJFPF6zj0YNv6xUuy; __Secure-1PAPISID=MsqFPyKNSnLA6qpF/AJFPF6zj0YNv6xUuy; __Secure-3PAPISID=MsqFPyKNSnLA6qpF/AJFPF6zj0YNv6xUuy; ACCOUNT_CHOOSER=AFx_qI7mkYlfm4MT0f8K2uj9oDDCoFPMwOietP9S31lBl3OGMMvI_-aQMIUTSRH9nd_a2VUFdVCTu8mjTTWHqRiOWRE8X7HoBrApOblmg2d12VUJ15_sBB0; __Host-GAPS=1:LUFmJiG1rUJp8SYs-6VqhoqkXaIKwd9TJ3NFFzV6Rg0bT6-MPD5yLamgcMhBTsJ5mocoWSOmRDnh0_esPMwm_cNEmRLHZA:O1MzAUlaYbytgDzU"
    for c in str_cookie.split(";"):
        n, v = c.split("=", 1)
        n, v = n.strip(), v.strip()
        print(n,v)
        driver.add_cookie({"name": n, "value": v})

    driver.refresh()

    time.sleep(3)
    input("Press Enter to close browser...")

    driver.quit()