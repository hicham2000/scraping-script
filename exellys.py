import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup

job_titles = []
companies = []
locations = []
domains = []
types = []
countries = []
urls = []
driver = webdriver.Chrome()
cookies = 1

url  = "https://www.exellys.com/en-gb/jobs?page="
id = 1
for i in range(1,3):

    driver.get("https://www.exellys.com/en-gb/jobs?page=" + str(i)+"&vacature+country=The+Netherlands")

    if cookies == 1:
        cokie = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonAccept")))
        cokie.click()
        cookies = 0

    try:

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
    except Exception as e:
        print()

    div = driver.find_element(By.CLASS_NAME,"blockEntry")
    Articles = div.find_elements(By.TAG_NAME,"li")
    for ele in Articles:
        link = ele.find_element(By.TAG_NAME,"a")
        l = link.get_attribute("href")

        s = ele.find_element(By.CLASS_NAME,"widgetHeader")


        b = ele.find_element(By.CLASS_NAME, "widgetSubHeader")

        try:
            domains.append(b.text.split("•")[1])
            locations.append(b.text.split("•")[0])
            job_titles.append(s.text)
            countries.append("The Netherlands")
        except Exception as o:
            print()

        print(l)
        urls.append(l)


# div = driver.find_element(By.CLASS_NAME,"blockEntry")
# Articles = div.find_elements(By.TAG_NAME,"li")
#
# for ele in Articles:
#     a = ele.find_element(By.CLASS_NAME,"widgetHeader")
#     job_titles.append(a.text.split("-")[0])
#     companies.append(a.text.split("-")[1])
#     b = ele.find_element(By.CLASS_NAME,"widgetSubHeader")
#     locations.append(b.text.split("•")[0])
#     domains.append(b.text.split("•")[1])
#     print("***********")

urls = [item for item in urls if item != "https://www.exellys.com/advert"]

print(len(urls))
print(len(job_titles))
print(len(domains))
print(len(locations))

for l in urls:


    driver.get(l)
    try:
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
    except Exception as e:
        print()

    z = driver.find_element(By.CLASS_NAME,"header")
    a = driver.find_elements(By.TAG_NAME,"h1")

    e = driver.find_element(By.CLASS_NAME,"widgetSubHeader")
    f = e.find_element(By.TAG_NAME,"span")
    print(f.text)
    types.append(f.text)

    n = driver.find_element(By.CLASS_NAME,"content")
    companies.append(n.text.split(" ")[0])

    print("ok")



data = {
        "JOB_TITLE": job_titles,
        "COMPANY": companies,
        "LOCATION": locations,
        "DOMAIN": domains,
        "CAREER_TYPE": types,
        "COUNTRY": countries,
        "URL": urls

    }
df = pd.DataFrame(data)
# Export the DataFrame to an Excel file
df.to_excel("exellys_1.xlsx", index=False)

