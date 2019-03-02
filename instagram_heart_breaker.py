from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("./chromedriver")

driver.get("http://instagram.com/")
btn_name = driver.find_element_by_link_text("로그인")
btn_name.click()

time.sleep(2)

element = driver.find_element_by_name("username")
element.send_keys("dlwnsgml91")

element = driver.find_element_by_name("password")
element.send_keys("wnsgml337!")
element.send_keys(Keys.RETURN)

time.sleep(2)
driver.find_element_by_class_name("HoLwm ").click()

element = driver.find_element_by_class_name(" x3qfX ")
action = ActionChains(driver)
action.move_to_element(element)
action.click()
element.send_keys("#태형")
time.sleep(2)
action.perform()

time.sleep(2)

action.reset_actions()
action.move_by_offset(0, 50)
action.click()
action.perform()
# input()

time.sleep(5)

element = driver.find_element_by_class_name("EZdmt")
posts = driver.find_elements_by_class_name("_9AhH0")
action = ActionChains(driver)

for post in posts:
    action.reset_actions()
    action.move_to_element(post)
    action.click()
    action.perform()

    time.sleep(3)

    try:
        element = driver.find_element_by_class_name("fr66n")
        element.click()
    except:
        pass

    action.reset_actions()
    action.send_keys(Keys.ESCAPE)
    action.perform()

    time.sleep(1)


input()
