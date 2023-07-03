import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from bs4 import BeautifulSoup

import time


def web_scrape_contents(driver):
#     driver = create_service()
#     soup=get_weburl_contents()
#     click_checkbox(driver)
#     date = soup.find("p",{"class":"text-center uppercase leading-7"}).find("span",attrs={"class":"bg-[#282828] px-3 py-1 text-highlight md:py-3"})
#     title_qs = soup.find("div",{"class":"css-1fsj6j6 ey5cnfx3"}).find("h1",attrs={"class":"bg-[#282828] px-2 py-6 text-3xl font-bold text-gray-200 md:text-4xl lg:text-5xl"}).text
    test1=driver.find_elements(By.XPATH, "//span[@class='css-1djf0pi e12e3var0']")
    question=test1[0].text

    ops1=test1[1].text
    ops2=test1[2].text
    ops3=test1[3].text
    ops4=test1[4].text

    ans=test1[5].text

    ref=test1[6].text
    
#     urls links
    url1=driver.find_elements(By.XPATH, "//span[@class='css-1djf0pi e12e3var0']/ul/li/a")
    urls_ops=[]
    for urls in url1:
        urls_ops.append(urls.get_attribute("href"))
    
    d={
      'question':question,
      'Option1':ops1,
      'Option2':ops2,
      'Option3':ops3,
      'Option4':ops4,
      'answer':ans,
      'references':ref,
      'urls_list':[urls_ops]}
    
    return d

def scrape():
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    # Create service
    webdriver_service = Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=webdriver_service,options = chrome_options)
    page_url = "https://today.bnomial.com/"
    driver.get(page_url)
    driver.maximize_window()


    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label//input[@type='checkbox']"))).click()
    except Exception:
        pass
    finally:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label//input[@type='checkbox']"))).click()

        
        
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button"))).click()
    except Exception:
        pass
    finally:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button"))).click()
        
    print("Success") 
    return driver
    
if __name__ == "__main__":
    driver=scrape()   
    time.sleep(1)
    row=web_scrape_contents(driver)
    print(row)

