from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd







chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

cookies = 1
articles = []
headlines = []
dates = []
times = []
links = []
texts = []
Company_Names = []
tickerSymbols = []
dividends = []
pe_ratios = []
prices_moved = []

skip = 0

Yahoo_url = "https://uk.finance.yahoo.com/quote/"

url = "https://www.londonstockexchange.com/news?tab=today-s-news"

driver.get(url)



try:
    # Wait for the "Accept Cookies" button to be clickable and click it
    if cookies == 1:

        cokie = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ccc-notify-accept")))
        cokie.click()
        cookies = 0

    try:

        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
    except Exception as e:
        print()
    # Extract news articles

    Articles = driver.find_elements(By.CLASS_NAME, "medium-font-weight")

    for skip, article in enumerate(Articles):
        if skip >= 2:
            title = article.text.split("\n")

            # Check if the title has at least 2 elements before accessing them
            if len(title) >= 2:
                date = title[1].split(" ")[1]
                time = title[1].split(" ")[2]

                headlines.append(title[0])
                dates.append(date)
                times.append(time)

                link_element = article.find_element(By.CLASS_NAME, "dash-link")
                link = link_element.get_attribute("href")
                links.append(link)

        skip = skip + 1



except Exception as e:
    print("Error:", e)


cookies = 1
i = 0
for ele in links:
    driver.get(ele)
    try:
        status_box = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "status-box-content")))
        status_box.click()

        try:

            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
        except Exception as e:
            print()

        # Find the <div> element with the attribute itemprop="articleBody"
        # Get the text inside the <div> element
        head = driver.find_element(By.CLASS_NAME, "news-article-content-body")
        texts.append(head.text)
        try:
            Company_Name = driver.find_element(By.XPATH, "//a[@itemprop='author']")
            Company_Names.append(Company_Name.text)
            company_Name_link = Company_Name.get_attribute("href")
            driver.get(company_Name_link)

            try:

                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
            except Exception as e:
                print()
            tickerSymbol = driver.find_element(By.XPATH, "//span[@itemprop='tickerSymbol']")

            tickerSymbols.append(tickerSymbol.text)

        except Exception as e:
            Company_Name = "N/A"
            Company_Names.append(Company_Name)
            tickerSymbol = "N/A"
            tickerSymbols.append(tickerSymbol)

    except Exception as e:

        head = driver.find_element(By.CLASS_NAME, "news-article-content-body")
        texts.append(head.text)
        try:
            try:
                Company_Name = driver.find_element(By.XPATH, "//a[@itemprop='author']")
                Company_Names.append(Company_Name.text)
                company_Name_link = Company_Name.get_attribute("href")
                driver.get(company_Name_link)
            except Exception as e:
                Company_Name = "N/A"
                Company_Names.append(Company_Name)

            try:
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
            except Exception as e:
                print()

            try:
                tickerSymbol = driver.find_element(By.XPATH, "//span[@itemprop='tickerSymbol']")
                if tickerSymbol.text.endswith("."):
                    ticker = tickerSymbol.text.rstrip('.')
                    tickerSymbols.append(ticker)
                else:
                    ticker = tickerSymbol.text
                    tickerSymbols.append(ticker)

            except Exception as e:
                tickerSymbol = "N/A"
                tickerSymbols.append(tickerSymbol)

            if tickerSymbol != "N/A":
                Yahoo_link = Yahoo_url + ticker + ".L"
                driver.get(Yahoo_link)
                if cookies == 1:
                    cokie = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "accept-all")))
                    cokie.click()
                    cookies = 0
                try:

                    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "break")))
                except Exception as e:
                    print()
                try:
                    dividend = driver.find_element(By.XPATH, "//td[@data-test='DIVIDEND_AND_YIELD-value']")
                    dividends.append(dividend.text.split(" ")[1])
                except Exception as e:
                    dividends.append("N/A")

                try:
                    pe_ratio = driver.find_element(By.XPATH, "//td[@data-test='PE_RATIO-value']")
                    pe_ratios.append(pe_ratio.text)
                except Exception as e:
                    pe_ratios.append("N/A")
                try:
                    parent_div = driver.find_element(By.ID,"quote-header-info")
                    price_moved = parent_div.find_elements(By.TAG_NAME, "fin-streamer")
                    prices_moved.append(price_moved[2].text)

                except Exception as e:
                    prices_moved.append("N/A")
            else:
                dividends.append("N/A")
                pe_ratios.append("N/A")
                prices_moved.append("N/A")

        except Exception as e:
            print()





    print(f"{times[i]} - {dates[i]} - {tickerSymbols[i]} - {Company_Names[i]} - {headlines[i]} - {pe_ratios[i]} - {dividends[i]} - {prices_moved[i]} - {links[i]}")

    print(texts[i])
    print("\n\n*********************************************************************************************************")
    print("*********************************************************************************************************")
    print("*********************************************************************************************************\n\n")

    i = i + 1


data = {
        "Date": dates,
        "Time": times,
        "Ticker": tickerSymbols,
        "Company Name": Company_Names,
        "Headline": headlines,
        "PE ratio": pe_ratios,
        "Dividend Yield": dividends,
        "URL": links,
        "price moved": prices_moved
    }
df = pd.DataFrame(data)
# Export the DataFrame to an Excel file
df.to_excel("londonstockexchange.xlsx", index=False)