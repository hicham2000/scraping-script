from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://hbr.org/search?term=connection&loaded=41")

#driver.get("https://hbr.org/search?term=connection")


titles = []
categories = []
owners = []
dates = []
prices = []
links = []
description = []



Articles = driver.find_elements(By.CLASS_NAME, "stream-entry")

i = 0
for article in Articles:
    try:
        title = article.find_element(By.CLASS_NAME, "hed")
        titles.append(title.text)

    except Exception as e:
        titles.append("N/A")

    try:
        link = title.find_element(By.TAG_NAME,"a")
        links.append(link.get_attribute("href"))

    except Exception as e:
        links.append("N/A")

    try:
        category = article.find_element(By.CLASS_NAME, "topic")
        categories.append(category.text)
    except Exception as e:
        categories.append("N/A")

    try:
        owner = article.find_element(By.CLASS_NAME, "byline")
        owners.append(owner.text)
    except Exception as e:
        owners.append("N/A")

    try:
        date = article.find_element(By.CLASS_NAME, "pubdate")
        dates.append(date.text)

    except Exception as e:
        dates.append("N/A")


    try:
        price = article.find_element(By.CLASS_NAME,"price")
        prices.append(price.text + " $")

    except Exception as e:
        prices.append("N/A")

    print(titles[i] + " - " + categories[i] + " - " + owners[i] + " - " + dates[i] + " - " + prices[i] + " - " )
    i = i + 1



print(i)

for ele in links:
    driver.get(ele)
    print(ele)
    try:
        Des = driver.find_element(By.CLASS_NAME, "productView-description")
        description.append(Des.text)

    except Exception as e:
        try:
            Des = driver.find_element(By.XPATH, "//div[@js-target='article-content-flex2019']")
            description.append(Des.text)
        except Exception as e:
            description.append("N/A")
data = {
        "Title": titles,
        "Category": categories,
        "Owner": owners,
        "Date": dates,
        "Price": prices,
        "Link": links,
        "description": description
    }
df = pd.DataFrame(data)
# Export the DataFrame to an Excel file
df.to_excel("HbrArticles.xlsx", index=False)