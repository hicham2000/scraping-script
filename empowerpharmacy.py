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


def download(type,folder_name,j):
    file_name =str(j) + "."+ type
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    path = os.path.join(folder_name, file_name)

    response = requests.get(imglink)
    if response.ok:
        with open(path, 'wb') as f:
            f.write(response.content)
            print(f"Image saved successfully in '{folder_name}' folder as '{file_name}'.")

    else:
        print("Failed to download the image.")


folder_name = "images"
id = 1
names = []
ids = []
links = []
imglinks = []

Dosage = []
CDosage = []
GeneralInformation = []
CGeneralInformation = []
MechanismsofAction = []
CMechanismsofAction = []
ContraindicationsPrecautions = []
CContraindicationsPrecautions = []
Pregnancy = []
CPregnancy = []
BreastFeeding = []
CBreastFeeding = []
AdverseReactions = []
CAdverseReactions = []
Storage = []
CStorage = []

driver = webdriver.Chrome()

driver.get("https://www.empowerpharmacy.com/drug-catalog")

try:

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
except Exception as e:
    print()


articles = driver.find_elements(By.CLASS_NAME,"image-column")

for ele in articles:

    image = ele.find_element(By.TAG_NAME,"img")
    name = ele.find_elements(By.TAG_NAME,"a")[1]
    names.append(name.text)
    ids.append(id)
    imglink = image.get_attribute("src")
    imglinks.append(imglink)

    link = ele.find_elements()
    productUrl = name.get_attribute("href")
    links.append(productUrl)


    id = id+1

id = 1
for link in links:
    print(id)
    print(link)
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the specific div element using its attributes or class
    try:
        #target_div = soup.find("dl")
        #descriptions.append(target_div.text)
        target_div = soup.find("dl")
        element = target_div.find_all("dt")
        ele = target_div.find_all("dd")
        if (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanisms of Action" and
                a(element[3].text) == "Contraindications / Precautions" and a(element[4].text) == "Pregnancy" and
                a(element[5].text) == "Breast Feeding"  and
                a(element[7].text) == "Adverse Reactions / Side Effects" and a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append(a(element[5].text))
            BreastFeeding.append(a(ele[5].text))
            CAdverseReactions.append(a(element[7].text))
            AdverseReactions.append(a(ele[7].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(element[4].text) == "Pregnancy" and
              a(element[5].text) == "Breastfeeding" and a(element[6].text) == "Adverse Reactions/Side Effects" and a(
                    element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append(a(element[5].text))
            BreastFeeding.append(a(ele[5].text))
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))
        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[4].text) == "Contraindications/Precautions" and a(element[5].text) == "Pregnancy" and
              a(element[6].text) == "Breast-feeding" and
              a(element[8].text) == "Adverse Reactions/Side Effects" and a(element[9].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append(a(element[6].text))
            BreastFeeding.append(a(ele[6].text))
            CAdverseReactions.append(a(element[8].text))
            AdverseReactions.append(a(ele[8].text))
            CStorage.append(a(element[9].text))
            Storage.append(a(ele[9].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(element[4].text) == "Pregnancy" and
              a(element[5].text) == "Breastfeeding" and
              a(element[7].text) == "Adverse Reactions/Side Effects" and a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append(a(element[5].text))
            BreastFeeding.append(a(ele[5].text))
            CAdverseReactions.append(a(element[7].text))
            AdverseReactions.append(a(ele[7].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))
        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(element[4].text) == "Pregnancy" and
              a(element[5].text) == "Breastfeeding" and
              a(element[7].text) == "Adverse Reactions/Side Effects" and a(element[9].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append(a(element[5].text))
            BreastFeeding.append(a(ele[5].text))
            CAdverseReactions.append(a(element[7].text))
            AdverseReactions.append(a(ele[7].text))
            CStorage.append(a(element[9].text))
            Storage.append(a(ele[9].text))
        elif (a(element[1].text) == "General Information" and
              a(element[3].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append("N/A")
            MechanismsofAction.append("N/A")
            CContraindicationsPrecautions.append("N/A")
            ContraindicationsPrecautions.append("N/A")
            CPregnancy.append("N/A")
            Pregnancy.append("N/A")
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append("N/A")
            AdverseReactions.append("N/A")
            CStorage.append(a(element[3].text))
            Storage.append(a(ele[3].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications and Precautions" and a(element[4].text) == "Pregnancy" and
              a(element[5].text) == "Breast-feeding" and
              a(element[6].text) == "Adverse Reactions" and a(element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append(a(element[5].text))
            BreastFeeding.append(a(ele[5].text))
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))
        elif (a(element[1].text) == "General Information" and

              a(element[4].text) == "Adverse Reactions/Side Effects" and a(element[5].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append("N/A")
            MechanismsofAction.append("N/A")
            CContraindicationsPrecautions.append("N/A")
            ContraindicationsPrecautions.append("N/A")
            CPregnancy.append("N/A")
            Pregnancy.append("N/A")
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[4].text))
            AdverseReactions.append(a(ele[4].text))
            CStorage.append(a(element[5].text))
            Storage.append(a(ele[5].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[4].text) == "Contraindications/Precautions" and a(element[5].text) == "Pregnancy" and
              a(element[6].text) == "Breastfeeding" and
              a(element[8].text) == "Adverse Reactions/Side Effects" and a(element[9].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append(a(element[6].text))
            BreastFeeding.append(a(ele[6].text))
            CAdverseReactions.append(a(element[8].text))
            AdverseReactions.append(a(ele[8].text))
            CStorage.append(a(element[9].text))
            Storage.append(a(ele[9].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(element[4].text) == "Pregnancy" and
              a(element[5].text) == "Breast-feeding" and
              a(element[7].text) == "Adverse Reactions/Side Effects" and a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append(a(element[5].text))
            BreastFeeding.append(a(ele[5].text))
            CAdverseReactions.append(a(element[7].text))
            AdverseReactions.append(a(ele[7].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))
        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[5].text) == "Contraindications/Precautions" and a(element[6].text) == "Pregnancy" and
              a(element[7].text) == "Breast-feeding" and
              a(element[8].text) == "Adverse Reactions/Side Effects" and a(element[9].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[5].text))
            ContraindicationsPrecautions.append(a(ele[5].text))
            CPregnancy.append(a(element[6].text))
            Pregnancy.append(a(ele[6].text))
            CBreastFeeding.append(a(element[7].text))
            BreastFeeding.append(a(ele[7].text))
            CAdverseReactions.append(a(element[8].text))
            AdverseReactions.append(a(ele[8].text))
            CStorage.append(a(element[9].text))
            Storage.append(a(ele[9].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[4].text) == "Contraindications/Precautions" and a(element[5].text) == "Pregnancy" and
              a(element[6].text) == "Breast-Feeding" and
              a(element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append(a(element[6].text))
            BreastFeeding.append(a(ele[6].text))
            CAdverseReactions.append("N/A")
            AdverseReactions.append("N/A")
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(
                    element[4].text) == "Pregnancy/Breastfeeding" and

              a(element[6].text) == "Adverse Reactions/Side Effects" and a(element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[5].text) == "Contraindications/Precautions" and a(element[6].text) == "Pregnancy" and
              a(element[7].text) == "Breast-Feeding" and a(element[9].text) == "Adverse Reactions/Side Effects" and
              a(element[10].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[5].text))
            ContraindicationsPrecautions.append(a(ele[5].text))
            CPregnancy.append(a(element[6].text))
            Pregnancy.append(a(ele[6].text))
            CBreastFeeding.append(a(element[7].text))
            BreastFeeding.append(a(ele[7].text))
            CAdverseReactions.append(a(element[9].text))
            AdverseReactions.append(a(ele[9].text))
            CStorage.append(a(element[10].text))
            Storage.append(a(ele[10].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[5].text) == "Contraindications/Precautions" and a(element[6].text) == "Pregnancy" and
              a(element[7].text) == "Breast-Feeding" and a(element[8].text) == "Adverse Reactions/Side Effects" and
              a(element[9].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[5].text))
            ContraindicationsPrecautions.append(a(ele[5].text))
            CPregnancy.append(a(element[6].text))
            Pregnancy.append(a(ele[6].text))
            CBreastFeeding.append(a(element[7].text))
            BreastFeeding.append(a(ele[7].text))
            CAdverseReactions.append(a(element[8].text))
            AdverseReactions.append(a(ele[8].text))
            CStorage.append(a(element[9].text))
            Storage.append(a(ele[9].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[4].text) == "Contraindications/Precautions" and a(element[5].text) == "Pregnancy" and
              a(element[6].text) == "Breast-Feeding" and a(element[7].text) == "Adverse Reactions/Side Effects" and
              a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append(a(element[6].text))
            BreastFeeding.append(a(ele[6].text))
            CAdverseReactions.append(a(element[7].text))
            AdverseReactions.append(a(ele[7].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[4].text) == "Contraindications/Precautions" and a(
                    element[5].text) == "Pregnancy / Breastfeeding" and

              a(element[6].text) == "Adverse Reactions/Side Effects" and a(element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))
        elif (a(element[1].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append("N/A")
            GeneralInformation.append("N/A")
            CMechanismsofAction.append("N/A")
            MechanismsofAction.append("N/A")
            CContraindicationsPrecautions.append("N/A")
            ContraindicationsPrecautions.append("N/A")
            CPregnancy.append("N/A")
            Pregnancy.append("N/A")
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append("N/A")
            AdverseReactions.append("N/A")
            CStorage.append(a(element[1].text))
            Storage.append(a(ele[1].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[4].text) == "Contraindications/Precautions" and a(element[5].text) == "Pregnancy" and
              a(element[6].text) == "Breast-feeding" and a(element[7].text) == "Adverse Reactions/Side Effects" and
              a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append(a(element[6].text))
            BreastFeeding.append(a(ele[6].text))
            CAdverseReactions.append(a(element[7].text))
            AdverseReactions.append(a(ele[7].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))

        elif (a(element[1].text) == "General Information" and
              a(element[2].text) == "Contraindications/Precautions" and a(element[3].text) == "Pregnancy" and
              a(element[4].text) == "Breastfeeding" and a(element[5].text) == "Adverse Reactions/Side Effects" and
              a(element[6].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append("N/A")
            MechanismsofAction.append("N/A")
            CContraindicationsPrecautions.append(a(element[2].text))
            ContraindicationsPrecautions.append(a(ele[2].text))
            CPregnancy.append(a(element[3].text))
            Pregnancy.append(a(ele[3].text))
            CBreastFeeding.append(a(element[4].text))
            BreastFeeding.append(a(ele[4].text))
            CAdverseReactions.append(a(element[5].text))
            AdverseReactions.append(a(ele[5].text))
            CStorage.append(a(element[6].text))
            Storage.append(a(ele[6].text))

        elif (a(element[1].text) == "General Information" and
              a(element[2].text) == "Contraindications/Precautions" and
              a(element[3].text) == "Adverse Reactions/Side Effects" and
              a(element[4].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append("N/A")
            MechanismsofAction.append("N/A")
            CContraindicationsPrecautions.append(a(element[2].text))
            ContraindicationsPrecautions.append(a(ele[2].text))
            CPregnancy.append("N/A")
            Pregnancy.append("N/A")
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[3].text))
            AdverseReactions.append(a(ele[3].text))
            CStorage.append(a(element[4].text))
            Storage.append(a(ele[4].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(
                    element[4].text) == "Pregnancy / Breastfeeding" and
              a(element[6].text) == "Adverse Reactions/Side Effects" and
              a(element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications / Precautions" and a(
                    element[4].text) == "Pregnancy / Breastfeeding" and
              a(element[6].text) == "Adverse Reactions/Side Effects" and
              a(element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[4].text) == "Contraindications/Precautions" and a(element[5].text) == "Pregnancy" and
              a(element[6].text) == "Breast-Feeding" and a(element[7].text) == "Adverse Reactions/Side Effects" and
              a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append(a(element[6].text))
            BreastFeeding.append(a(ele[6].text))
            CAdverseReactions.append(a(element[7].text))
            AdverseReactions.append(a(ele[7].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[4].text) == "Contraindications/Precautions" and a(element[5].text) == "Pregnancy" and
              a(element[6].text) == "Breast-Feeding" and a(element[8].text) == "Adverse Reactions/Side Effects" and
              a(element[9].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append(a(element[6].text))
            BreastFeeding.append(a(ele[6].text))
            CAdverseReactions.append(a(element[8].text))
            AdverseReactions.append(a(ele[8].text))
            CStorage.append(a(element[9].text))
            Storage.append(a(ele[9].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[6].text) == "Contraindications/Precautions" and a(
                    element[3].text) == "Pregnancy/Breastfeeding" and
              a(element[5].text) == "Adverse Reactions/Side Effects" and
              a(element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[6].text))
            ContraindicationsPrecautions.append(a(ele[6].text))
            CPregnancy.append(a(element[3].text))
            Pregnancy.append(a(ele[3].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[5].text))
            AdverseReactions.append(a(ele[5].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(
                    element[4].text) == "Pregnancy/Breastfeeding" and
              a(element[5].text) == "Adverse Reactions/Side Effects" and
              a(element[6].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[5].text))
            AdverseReactions.append(a(ele[5].text))
            CStorage.append(a(element[6].text))
            Storage.append(a(ele[6].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications / Precautions" and a(
                    element[4].text) == "Pregnancy / Breastfeeding" and
              a(element[6].text) == "Adverse Reactions / Side Effects" and a(
                    element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanisms of Action" and
              a(element[6].text) == "Contraindications/Precautions" and a(
                    element[3].text) == "Pregnancy/Breastfeeding" and
              a(element[5].text) == "Adverse Reactions/Side Effects" and a(
                    element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[6].text))
            ContraindicationsPrecautions.append(a(ele[6].text))
            CPregnancy.append(a(element[3].text))
            Pregnancy.append(a(ele[3].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[5].text))
            AdverseReactions.append(a(ele[5].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanisms of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(
                    element[4].text) == "Pregnancy/Breastfeeding" and
              a(element[5].text) == "Adverse Reactions/Side Effects" and a(
                    element[6].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[5].text))
            AdverseReactions.append(a(ele[5].text))
            CStorage.append(a(element[6].text))
            Storage.append(a(ele[6].text))

        elif (a(element[1].text) == "General Information" and a(
                element[4].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append("N/A")
            MechanismsofAction.append("N/A")
            CContraindicationsPrecautions.append("N/A")
            ContraindicationsPrecautions.append("N/A")
            CPregnancy.append("N/A")
            Pregnancy.append("N/A")
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append("N/A")
            AdverseReactions.append("N/A")
            CStorage.append(a(element[4].text))
            Storage.append(a(ele[4].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(element[4].text) == "Pregnancy" and
              a(element[5].text) == "Breastfeeding" and a(element[6].text) == "Adverse Reactions/Side Effects" and
              a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append(a(element[5].text))
            BreastFeeding.append(a(ele[5].text))
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanisms of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(
                    element[4].text) == "Pregnancy/Breastfeeding" and
              a(element[6].text) == "Adverse Reactions/Side Effects" and
              a(element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[4].text) == "Contraindications/Precautions" and a(
                    element[5].text) == "Pregnancy/Breastfeeding" and
              a(element[7].text) == "Adverse Reactions/Side Effects" and
              a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[7].text))
            AdverseReactions.append(a(ele[7].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications" and a(element[4].text) == "Pregnancy" and
              a(element[5].text) == "Breastfeeding" and a(element[6].text) == "Adverse Reactions/Side Effects" and
              a(element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append(a(element[5].text))
            BreastFeeding.append(a(ele[5].text))
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[5].text) == "Contraindications/Precautions" and a(element[6].text) == "Pregnancy" and
              a(element[7].text) == "Breastfeeding" and
              a(element[9].text) == "Adverse Reactions/Side Effects" and a(element[10].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[5].text))
            ContraindicationsPrecautions.append(a(ele[5].text))
            CPregnancy.append(a(element[6].text))
            Pregnancy.append(a(ele[6].text))
            CBreastFeeding.append(a(element[7].text))
            BreastFeeding.append(a(ele[7].text))
            CAdverseReactions.append(a(element[9].text))
            AdverseReactions.append(a(ele[9].text))
            CStorage.append(a(element[10].text))
            Storage.append(a(ele[10].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[5].text) == "Contraindications/Precautions" and a(element[6].text) == "Pregnancy" and
              a(element[7].text) == "Breastfeeding" and
              a(element[8].text) == "Adverse Reactions/Side Effects" and a(element[9].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[5].text))
            ContraindicationsPrecautions.append(a(ele[5].text))
            CPregnancy.append(a(element[6].text))
            Pregnancy.append(a(ele[6].text))
            CBreastFeeding.append(a(element[7].text))
            BreastFeeding.append(a(ele[7].text))
            CAdverseReactions.append(a(element[8].text))
            AdverseReactions.append(a(ele[8].text))
            CStorage.append(a(element[9].text))
            Storage.append(a(ele[9].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(element[4].text) == "Pregnancy" and
              a(element[5].text) == "Breastfeeding" and
              a(element[8].text) == "Adverse Reactions/Side Effects" and a(element[9].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append(a(element[5].text))
            BreastFeeding.append(a(ele[5].text))
            CAdverseReactions.append(a(element[8].text))
            AdverseReactions.append(a(ele[8].text))
            CStorage.append(a(element[9].text))
            Storage.append(a(ele[9].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[4].text) == "Contraindications/Precautions" and a(element[5].text) == "Pregnancy" and
              a(element[6].text) == "Breastfeeding" and
              a(element[9].text) == "Adverse Reactions/Side Effects" and a(element[10].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append(a(element[6].text))
            BreastFeeding.append(a(ele[6].text))
            CAdverseReactions.append(a(element[9].text))
            AdverseReactions.append(a(ele[9].text))
            CStorage.append(a(element[10].text))
            Storage.append(a(ele[10].text))

        elif (a(element[7].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append("N/A")
            GeneralInformation.append("N/A")
            CMechanismsofAction.append("N/A")
            MechanismsofAction.append("N/A")
            CContraindicationsPrecautions.append("N/A")
            ContraindicationsPrecautions.append("N/A")
            CPregnancy.append("N/A")
            Pregnancy.append("N/A")
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append("N/A")
            AdverseReactions.append("N/A")
            CStorage.append(a(element[7].text))
            Storage.append(a(ele[7].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications/Precautions" and a(element[4].text) == "Pregnancy/Lactation" and
              a(element[5].text) == "Adverse Reactions/Side Effects" and
              a(element[6].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[5].text))
            AdverseReactions.append(a(ele[5].text))
            CStorage.append(a(element[6].text))
            Storage.append(a(ele[6].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[5].text) == "Contraindications/Precautions" and a(element[6].text) == "Pregnancy" and
              a(element[7].text) == "Breast-feeding" and
              a(element[9].text) == "Adverse Reactions/Side Effects" and a(element[10].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[5].text))
            ContraindicationsPrecautions.append(a(ele[5].text))
            CPregnancy.append(a(element[6].text))
            Pregnancy.append(a(ele[6].text))
            CBreastFeeding.append(a(element[7].text))
            BreastFeeding.append(a(ele[7].text))
            CAdverseReactions.append(a(element[9].text))
            AdverseReactions.append(a(ele[9].text))
            CStorage.append(a(element[10].text))
            Storage.append(a(ele[10].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications and Precautions" and a(
                    element[4].text) == "Pregnancy/Breastfeeding" and

              a(element[5].text) == "Adverse Reactions/Side Effects" and a(element[6].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[5].text))
            AdverseReactions.append(a(ele[5].text))
            CStorage.append(a(element[6].text))
            Storage.append(a(ele[6].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanisms of Action" and
              a(element[5].text) == "Contraindications/Precautions" and a(
                    element[6].text) == "Pregnancy/Breastfeeding" and

              a(element[7].text) == "Adverse Reactions/Side Effects" and a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[5].text))
            ContraindicationsPrecautions.append(a(ele[5].text))
            CPregnancy.append(a(element[6].text))
            Pregnancy.append(a(ele[6].text))
            CBreastFeeding.append("N/A")
            BreastFeeding.append("N/A")
            CAdverseReactions.append(a(element[7].text))
            AdverseReactions.append(a(ele[7].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))

        elif (a(element[1].text) == "General Information" and a(element[2].text) == "Mechanism of Action" and
              a(element[3].text) == "Contraindications / Precautions" and a(element[4].text) == "Pregnancy" and a(
                    element[5].text) == "Breastfeeding" and

              a(element[6].text) == "Adverse Reactions/Side Effects" and a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append(a(element[2].text))
            MechanismsofAction.append(a(ele[2].text))
            CContraindicationsPrecautions.append(a(element[3].text))
            ContraindicationsPrecautions.append(a(ele[3].text))
            CPregnancy.append(a(element[4].text))
            Pregnancy.append(a(ele[4].text))
            CBreastFeeding.append(a(element[5].text))
            BreastFeeding.append(a(ele[5].text))
            CAdverseReactions.append(a(element[6].text))
            AdverseReactions.append(a(ele[6].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))

        elif (a(element[1].text) == "General Information" and
              a(element[4].text) == "Contraindications/Precautions" and a(element[5].text) == "Pregnancy" and a(
                    element[6].text) == "Breastfeeding" and

              a(element[7].text) == "Adverse Reactions/Side Effects" and a(element[8].text) == "Storage"):
            print("ok")
            CDosage.append(a(element[0].text))
            Dosage.append(a(ele[0].text))
            CGeneralInformation.append(a(element[1].text))
            GeneralInformation.append(a(ele[1].text))
            CMechanismsofAction.append("N/A")
            MechanismsofAction.append("N/A")
            CContraindicationsPrecautions.append(a(element[4].text))
            ContraindicationsPrecautions.append(a(ele[4].text))
            CPregnancy.append(a(element[5].text))
            Pregnancy.append(a(ele[5].text))
            CBreastFeeding.append(a(element[6].text))
            BreastFeeding.append(a(ele[6].text))
            CAdverseReactions.append(a(element[7].text))
            AdverseReactions.append(a(ele[7].text))
            CStorage.append(a(element[8].text))
            Storage.append(a(ele[8].text))

        else:
            print("non")


    except Exception as e:
        CDosage.append("")
        Dosage.append("")
        CGeneralInformation.append("N")
        GeneralInformation.append("")
        CMechanismsofAction.append("")
        MechanismsofAction.append("")
        CContraindicationsPrecautions.append("")
        ContraindicationsPrecautions.append("")
        CPregnancy.append("")
        Pregnancy.append("")
        CBreastFeeding.append("")
        BreastFeeding.append("")
        CAdverseReactions.append("")
        AdverseReactions.append("")
        CStorage.append("")
        Storage.append("")


    id = id + 1


data = {
        "id": ids,
        "name": names,
        "Images": imglinks,
        "Meta: general_Information": CGeneralInformation,
        "Meta: general_Information_data": GeneralInformation,
        "Meta: mechanism_of_action": CMechanismsofAction,
        "Meta: mechanism_of_action_data": MechanismsofAction,
        "Meta: contraindicationsperecautions": CContraindicationsPrecautions,
        "Meta: contraindicationsperecautions_data": ContraindicationsPrecautions,
        "Meta: pregnancy": CPregnancy,
        "Meta: pregnancy_data": Pregnancy,
        "Meta: breastfeeding": CBreastFeeding,
        "Meta: breastfeeding_data": BreastFeeding,
        "Meta: adverse_reactionsside_effects": CAdverseReactions,
        "Meta: adverse_reactionsside_effects_data": AdverseReactions,
        "Meta: storage": CStorage,
        "Meta: storage_data":Storage,
        "Meta: dosage_strength": CDosage,
        "Meta: dosage_strength_data":Dosage,
        "link": links


    }
df = pd.DataFrame(data)
# Export the DataFrame to an Excel file
df.to_excel("f4.xlsx", index=False)