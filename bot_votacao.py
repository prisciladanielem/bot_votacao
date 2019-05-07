from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()

browser.get('https://miaw.mtv.com.br/vote/artista-musical')

browser.maximize_window()

browser.implicitly_wait(20)

#anavitoria
#btn = browser.find_element_by_xpath('//*[@id="main"]/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[6]/div/div/div[3]/div/div[7]/div/button')
while True:
    btn = browser.find_element_by_xpath('//*[@id="main"]/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[6]/div/div/div[3]/div/div[1]/div/button')
    for b in range(20):
        btn.click()
        browser.implicitly_wait(2)
    browser.implicitly_wait(10)
    browser.refresh()