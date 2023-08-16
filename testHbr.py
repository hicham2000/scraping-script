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

def a(input_string):
    lines = input_string.splitlines()
    non_blank_lines = [line for line in lines if line.strip()]
    return '\n'.join(non_blank_lines)



response = requests.get('https://www.exellys.com/items/en-gb/vacancies/analysis/business-analist---apg')

soup = BeautifulSoup(response.content, "html.parser")

# Find the specific div element using its attributes or class
print(soup)





