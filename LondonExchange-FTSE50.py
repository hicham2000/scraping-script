from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1920, 1080)




cookies = 1
cookiess = 1
codes = []
names = []
marketcaps = []
prices = []
weekranges = []
yahoomarketcaps = []
PE_Ratios = []
ForwardDividendAndYields = []
sectors = []
industries = []

url = "https://www.londonstockexchange.com/indices/ftse-350/constituents/table?page="
yahooUrl = "https://finance.yahoo.com/quote/"



j = 0
for i in range(1,19):

    newUrl = url + str(i)
    driver.get(newUrl)
    if cookies == 1:

        cokie = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ccc-notify-accept")))
        cokie.click()
        cookies = 0

    try:

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
    except Exception as e:
        cookies = cookies

    Articles = driver.find_elements(By.CLASS_NAME,"slide-panel")

    for article in Articles:
        code = article.find_element(By.CLASS_NAME, "instrument-tidm")
        if code.text == "BT.A":
            codes.append("BT-A.L")
        elif code.text.endswith("."):
            code = code.text.rstrip(".")
            codes.append(code+".L")
        else:
            codes.append(code.text+".L")

        name = article.find_element(By.CLASS_NAME,"instrument-name")
        names.append(name.text)

        marketcap = article.find_element(By.CLASS_NAME, "instrument-marketcapitalization")
        marketcaps.append(marketcap.text)

        price = article.find_element(By.CLASS_NAME,"instrument-lastprice")
        prices.append(price.text)

        yahoo = yahooUrl + codes[j]
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(yahoo)


        if cookiess == 1:
            try:
                cokie = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "accept-all")))
                cokie.click()
                cookiess = 0
            except Exception as e:
                cookiess = 0

        try:

            WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
        except Exception as e:
            cookies = cookies

        try:
            weekrange = driver.find_element(By.XPATH, "//td[@data-test='FIFTY_TWO_WK_RANGE-value']")
            weekranges.append(weekrange.text)
        except Exception as e:
            weekranges.append("N/A")

        try:
            yahoomarketcap = driver.find_element(By.XPATH, "//td[@data-test='MARKET_CAP-value']")
            yahoomarketcaps.append(yahoomarketcap.text)
        except Exception as e:
            yahoomarketcaps.append("N/A")


        try:
            peratio = driver.find_element(By.XPATH, "//td[@data-test='PE_RATIO-value']")
            PE_Ratios.append(peratio.text)
        except Exception as e:
            PE_Ratios.append("N/A")

        try:
            ForwardDividendAndYield = driver.find_element(By.XPATH, "//td[@data-test='DIVIDEND_AND_YIELD-value']")
            ForwardDividendAndYields.append(ForwardDividendAndYield.text.split(" ")[1].replace("(", "").replace(")", "").replace("%", ""))
        except Exception as e:
            ForwardDividendAndYields.append("N/A")


        # Close the new tab
        driver.close()

        # Switch back to the original tab
        driver.switch_to.window(driver.window_handles[0])

        yahooProfil = yahooUrl+codes[j]+"/profile?p="+codes[j]
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(yahooProfil)
        try:

            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
        except Exception as e:
            cookies = cookies

        try:
            sector = driver.find_element(By.XPATH, "//p[@class='D(ib) Va(t)']/span[2]")
            sectors.append(sector.text)
        except Exception as e:
            sectors.append("N/A")

        try:
            industry = driver.find_element(By.XPATH, "//p[@class='D(ib) Va(t)']/span[4]")
            industries.append(industry.text)
        except Exception as e:
            industries.append("N/A")

        # Close the new tab
        driver.close()

        # Switch back to the original tab
        driver.switch_to.window(driver.window_handles[0])

        print(codes[j]+","+names[j]+","+marketcaps[j]+","+prices[j]+","+weekranges[j]+","+yahoomarketcaps[j]+","+PE_Ratios[j]+","+ForwardDividendAndYields[j]+","+sectors[j]+","+industries[j])


        j = j + 1

print(j)

data = {
        "Code": codes,
        "Name": names,
        "Market Cap ": marketcaps,
        "Price": prices,
        "52-week range": weekranges,
        "Yahoo Market cap": yahoomarketcaps,
        "PE Ratio": PE_Ratios,
        "Forward dividend & yield" : ForwardDividendAndYields,
        "Sector" : sectors,
        "Industry": industries
    }
df = pd.DataFrame(data)
# Export the DataFrame to an Excel file
df.to_excel("FTSE350.xlsx", index=False)
df.to_csv("FTSE350.csv", index=False)