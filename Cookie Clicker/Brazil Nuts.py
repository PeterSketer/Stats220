from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import tkinter as tk
import traceback
import keyboard
import time

"""
Add ability to click the secret achievements and open the debug menu with "Orteil" then "saysopensesame"

1. Name bakery Me saysopensesame
2. Rename bakery Orteil
3. Click lucky
4. Click golden cookie
5. Click x1k for cheat in range(42):
6. Click Ascend
7. Play as "Normal"


def cheating_on(driver):
    names = ["Me saysopensesame","Orteil","Cheater"]
    for name in names:
        actions = ActionChains(driver)
        change_name = driver.find_element_by_id('bakeryName')
        actions.click(change_name)
        actions.perform()
        bakery_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bakeryNameInput")))
        bakery_name.send_keys(name)
        bakery_name.send_keys(Keys.ENTER)

    dev_tools = driver.find_elements_by_class_name("option.neato")
    for i in range(3):
        
        fps = driver.find_element_by_id('fpsCounter')
        actions = ActionChains(driver)
        
        if i == 0:
            actions.move_to_element(fps)
            actions.click(dev_tools[23])
        elif i == 1:
            gold_cookie = driver.find_elements_by_class_name('shimmer')
            actions.click(gold_cookie[0])
        else:
            actions.move_to_element(fps)
            for i in range(35):
                actions.click(dev_tools[3])
        actions.perform()
    normal_run(driver, True)

    This might have to be a pipe dream. I can't make it click on the ascention upgrades
    #Click ascend id legacyButton the promptOption0
    ascender = driver.find_element_by_id('legacyButton')
    ascend_actions = ActionChains(driver)
    ascend_actions.click(ascender)
    ascend_actions.perform()
    ascend_actions.reset_actions()

    ascend_actions = ActionChains(driver)
    yes = driver.find_element_by_id('promptOption0')
    ascend_actions.click(yes)
    ascend_actions.perform()
    
    driver.implicitly_wait(10)
    all_ascentions = driver.find_elements_by_class_name("crate.upgrade.heavenly")
    ghosts = driver.find_elements_by_class_name("crate.upgrade.heavenly.ghosted")
    print("There are",len(all_ascentions),"Ascentions to get through")
    index = 0
    while ghosts:
        all_ascentions = driver.find_elements_by_class_name("crate.upgrade.heavenly")
        ghosts = driver.find_elements_by_class_name("crate.upgrade.heavenly.ghosted")
        ascend_actions = ActionChains(driver)
        if all_ascentions[index] in ghosts:
            continue
        else:
            ascend_actions.click(all_ascentions[index])
            ascend_actions.perform()
        index+=1
        """

def normal_run(driver, bulk):
    goldenTicket = 0
    running = True
    block = False
    go_time = True

    cookie = driver.find_element_by_id('bigCookie')

    if bulk:
        buy_bulk = driver.find_element_by_id('storeBulk100')
        purchase = ActionChains(driver)
        purchase.click(buy_bulk)
        purchase.perform()

    while running:
        if keyboard.is_pressed(" "):
            if block == False:
                block = True
                go_time = not go_time
                print("Paused!")
        else:
            block = False

        if go_time:
        
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
                find_sugar = driver.find_element_by_id('lumpsAmount')
                if int(find_sugar.text) >= 1:
                    
                    print("You have", find_sugar, "Sugar lumps available")
            except:
                continue

            cookie = driver.find_element_by_id('bigCookie')
            actions.double_click(cookie)
            actions.perform()
        else:
            pass

def main():

    """
    To Do list
    It's Empty !!! :D
    """
    
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    print(driver.title)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Hooray program began at", current_time)

    
    try:
        print("New Normal Run is 1.\nNew Cheating Run is 2.")
        print("Press Space to pause and unpause the game once running")
        choice = input("Enter number of choice: ")
        
        if choice == "1":
            normal_run(driver, False)
        elif choice == "2":
            cheating_on(driver)
        elif choice == "3":
            normal_run(driver, True)
        
    except Exception as e:
        then = datetime.now()
        current_time1 = then.strftime("%H:%M:%S")
        print("Oops program broke at", current_time1)
        print(e)
        traceback.print_exc()

main()



"""

    window = tk.Tk()
    normal_btn = tk.Button(text="Click for Normal Run!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    )
    normal_btn.bind("<Button-1>", normal_run(driver))
    normal_btn.pack()
    window.mainloop()
"""
