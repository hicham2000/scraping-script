from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome()

job_titles = []
Companies = []
locations = []
links = []
Descriptions = []

url = "https://www.indeed.com/jobs?q=automotive&l=United+States&pp=gQAAAAAAAAAAAAAAAAACDPBeXAADAAABAAA&vjk=e9d42f61d0ef16f4"

driver.get(url)

Articles = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")

for ele in Articles:
    link = ele.find_element(By.CLASS_NAME,"jcs-JobTitle")
    print(link.text)
