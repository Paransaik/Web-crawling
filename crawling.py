from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\Users\\Osstem\\Desktop\\Web-crawling\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://mcdonalds.co.kr')

go = driver.find_element(By.CSS_SELECTOR, "#commonSearchForm > div > div > button")
go.send_keys(Keys.RETURN)

search = driver.find_element(By.CSS_SELECTOR, "#commonSearchWord")
search.click()
search.send_keys('Bacon')
search.send_keys(Keys.RETURN)

selected = driver.find_element(By.CSS_SELECTOR, "#container > div.content > div.contArea > div > div > div:nth-child(3) > div > ul > li:nth-child(2) > a")
selected.click()

calo = driver.find_element(By.CSS_SELECTOR, "#container > div.content > div.contArea > div > div > div.viewCon > div:nth-child(1) > button")
calo.click()

result = driver.find_element(By.CSS_SELECTOR, "#toggle02 > table > tbody > tr:nth-child(1) > td:nth-child(4)")
result.click()
print(result.text)

