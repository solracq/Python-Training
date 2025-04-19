import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def chrome_interaction(web_site):
    service = Service('/Users/carlosquiroz/dev/python/Selenium/chromedriver')
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get(web_site)
    time.sleep(5)
    search_box = driver.find_element('title', 'Search')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)
    service.stop()
    driver.quit()

web_site = 'http://www.google.com/'
# chrome_interaction(web_site)

def chrome_geeksforgeeks():
    driver = webdriver.Chrome('/Users/carlosquiroz/dev/python/Selenium/chromedriver')
    driver.get("https://google.com/search?q=geeksforgeeks")
    searchbox = driver.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3')
    assert searchbox, "Cannot find search icon!"
    searchbox.click()
    time.sleep(5)

chrome_geeksforgeeks()