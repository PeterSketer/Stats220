from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import traceback


driver = webdriver.Chrome('./chromedriver')

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id('bigCookie')

print(driver.title)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Hooray program began at", current_time)

goldenTicket = 0

try:
    cookie = driver.find_element_by_id('bigCookie')
    
    while True:
        cookie = driver.find_element_by_id('bigCookie')
        all_ups = driver.find_elements_by_class_name("crate.upgrade.enabled")
        buyables = driver.find_elements_by_class_name("product.unlocked.enabled")
        gold_cookie = driver.find_elements_by_class_name('shimmer')
        
        actions = ActionChains(driver)

        actions.double_click(cookie)
        actions.perform()
        try:
            if len(gold_cookie) > 0:
                actions.click(gold_cookie[0])
                actions.move_to_element(cookie)
                actions.perform()
                goldenTicket += 1
                print("Hey Another Golden Cookie that's",goldenTicket)
                continue

            if len(buyables) >= 1:
                actions.click(buyables[-1])
                actions.perform()
                continue
                
            if len(all_ups) >= 1:
                actions.click(all_ups[0])
                actions.perform()
                continue
        except:
            continue
        
        cookie = driver.find_element_by_id('bigCookie')
        actions.double_click(cookie)
        actions.perform()
    
except Exception as e:
    then = datetime.now()
    current_time1 = then.strftime("%H:%M:%S")
    print("Oops program broke at", current_time1)
    print(e)
    traceback.print_exc()
