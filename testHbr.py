from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://hbr.org/2021/05/the-climate-equity-connection")

#driver.get("https://hbr.org/search?term=connection")


titles = []
categories = []
owners = []
dates = []
prices = []
links = []
description = []

titles.append("The Climate-Equity Connection")
categories.append("The Big Idea Series")
owners.append("Auden Schendler")
dates.append("May 13, 2021")
prices.append("N/A")
links.append("https://hbr.org/2021/05/the-climate-equity-connection")

Des = driver.find_element(By.XPATH, "//div[@js-target='article-content-flex2019']")
description.append(Des.text)

data = {
        "Title": titles,
        "Category": categories,
        "Owner": owners,
        "Date": dates,
        "Price": prices,
        "Link": links,
        "description":description
    }
df = pd.DataFrame(data)
# Export the DataFrame to an Excel file
df.to_excel("HbrArticles.xlsx", index=False)