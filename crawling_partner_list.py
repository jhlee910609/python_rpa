import ssl
import time

from openpyxl import Workbook
from selenium import webdriver


def move_to_scroll_down(last_height):
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        # break condition
        if new_height == last_height:
            break
        last_height = new_height

def mk_list():
    sheet = write_wb.create_sheet("파트너_리스트")
    sheet['A1'] = "파트너명"
    sheet['B1'] = "url"

def add_url(name, url):
    sheet = write_wb["파트너_리스트"]
    sheet.append([name, url])

def get_partner_list_from_web():
    divClass = driver.find_elements_by_class_name("list_partner")
    return divClass[1].find_elements_by_tag_name("li")

SCROLL_PAUSE_TIME = 1
write_wb = Workbook()
mk_list()
ssl._create_default_https_context = ssl._create_unverified_context
driver = webdriver.Chrome("./chromedriver")
driver.get("https://1boon.kakao.com/p/partner")
move_to_scroll_down(driver.execute_script("return document.body.scrollHeight"))
partner_list = get_partner_list_from_web()

for partner in partner_list:
    link = partner.find_element_by_class_name("link_partner").get_attribute("href")
    name = partner.find_element_by_class_name("inner_txt").text
    add_url(name, link)
    # print("%s, %s"%(link, name))

write_wb.save("./partner_list_2.xlsx")
driver.quit()



