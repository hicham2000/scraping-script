from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def download(type,folder_name,j):
    file_name = "image" + str(j) + "."+ type
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    path = os.path.join(folder_name, file_name)

    response = requests.get(link)
    if response.ok:
        with open(path, 'wb') as f:
            f.write(response.content)
            print(f"Image saved successfully in '{folder_name}' folder as '{file_name}'.")

    else:
        print("Failed to download the image.")


j= 1355
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

url = "https://imgflip.com/?page="
folder_name = "images"

for i in range(100 , 1000):
    print("----------Page"+str(i)+"------------------------")
    driver.get(url+str(i))
    articles = driver.find_elements(By.CLASS_NAME, "base-unit")
    for article in articles:
        try:
            img = article.find_element(By.CLASS_NAME,"base-img")
            link = img.get_attribute("src")
            if str(link).endswith("jpg"):
                download("jpg",folder_name,j)
                j = j+ 1

        except Exception as e:
            print()

        try:
            img = article.find_element(By.CLASS_NAME, "base-img")
            link = img.get_attribute("data-src")
            link = "https:" + link
            if str(link).endswith("gif"):
                download("gif", folder_name, j)
                j = j + 1
            if str(link).endswith("jpg"):
                download("jpg", folder_name, j)
                j = j + 1

        except Exception as e:
            print()







