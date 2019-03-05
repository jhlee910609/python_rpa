from multiprocessing.pool import Pool

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import ssl
import time

from openpyxl import Workbook
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
import multiprocessing as mp

from selenium.webdriver.remote.webelement import WebElement

from domain.PostData import PostData


def set_headless_opt():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    return options


def move_to_scroll_down(SCROLL_PAUSE_TIME, last_height):
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


def go_to_end(driver: webdriver.Chrome):
    while True:
        try:
            driver.find_element_by_class_name("btn_lst_more").click()
            time.sleep(2)
        except ElementNotVisibleException as e:
            print(e)
            print("> End page!")
            break


def get_all_content():
    return driver.find_elements_by_class_name("inner_feed_box")


def get_each_content(content: WebElement):
    data = PostData()
    data.series = content.find_element_by_class_name('ell').text
    data.title = content.find_element_by_class_name("tit_feed").text
    data.date = content.find_element_by_class_name("date_post").text
    data.view_count = content.find_element_by_class_name("view_post").text
    data.like_count = content.find_element_by_class_name("u_cnt").text
    data.url = content.find_element_by_class_name("link_end").get_attribute("href")
    data.reply_count = content.find_element_by_tag_name("em").text
    data.to_string()
    write_to_excel(data)


def write_to_excel(data: PostData):
    new_sheet.append([data.date, data.series, data.title, data.view_count, data.like_count, data.reply_count, data.url])


wb = Workbook()
new_sheet = wb.create_sheet("휴머니스트")

if __name__ == '__main__':
    print(">>> crawling start!")
    BASE_URL = "https://post.naver.com/my.nhn?memberNo=12466858"
    driver = webdriver.Chrome("./chromedriver", options=set_headless_opt())
    driver.get(BASE_URL)

    time.sleep(1)

    go_to_end(driver)
    for content in get_all_content():
        get_each_content(content)
    wb.save("./humanist.xlsx")

    # move_to_scroll_down(2, driver.execute_script("return document.body.scrollHeight"))
    print(">>> crawling end!")
