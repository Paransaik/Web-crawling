# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 1}  # 1이 허용, #2가 금지인 거 같음
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path='C:\\Users\\Osstem\\Desktop\\Web-crawling\\chromedriver.exe',
                          options=chrome_options)

# driver = webdriver.Chrome(executable_path='C:\\Users\\Osstem\\Desktop\\Web-crawling\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.instagram.com/kjk76/')

id = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')

id.send_keys('kmj9247@naver.com')

pwd = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pwd.send_keys('test1323!')

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login.click()

driver.implicitly_wait(5)
saveInfo = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')
saveInfo.click()

# images1 = driver.find_elements(By.CSS_SELECTOR, "#mount_0_0_wA > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m > section > main > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9o._abcm > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a > div > div._aagv")
images2 = driver.find_elements_by_class_name('_aa8k')
images2[0].click()

text = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]')
print(text)
# images3 = driver.find_elements_by_class_name('_aabd _aa8k _aanf')
# print(images1)
# print(images2)


# goaw = driver.find_elements(By.CSS_SELECTOR, "#mount_0_0_wA > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m > section > main > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9o._abcm > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a > div > div._aagv")
# goaw.click()

#
# search = driver.find_element(By.CSS_SELECTOR, '#mount_0_0_RM > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m > section > main > div > div > div > section > div > button')
# search.click()
# search.send_keys('Bacon')
# search.send_keys(Keys.RETURN)
#
# selected = driver.find_element(By.CSS_SELECTOR,
#                                "#container > div.content > div.contArea > div > div > div:nth-child(3) > div > ul > li:nth-child(2) > a")
# selected.click()
#
# calo = driver.find_element(By.CSS_SELECTOR,
#                            "#container > div.content > div.contArea > div > div > div.viewCon > div:nth-child(1) > button")
# calo.click()
#
# result = driver.find_element(By.CSS_SELECTOR, "#toggle02 > table > tbody > tr:nth-child(1) > td:nth-child(4)")
# result.click()
# print(goaw.text)
