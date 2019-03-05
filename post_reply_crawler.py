import datetime
import re
import ssl
import time

from openpyxl import load_workbook
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


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


def set_headless_opt():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    return options


def get_reply(reply_list):
    for temp in reply_list:
        name = temp.find_element_by_class_name('u_cbox_nick').text
        content = temp.find_element_by_class_name('u_cbox_contents').text
        like_count = temp.find_element_by_class_name('u_cbox_cnt_recomm').text
        unlike_count = temp.find_element_by_class_name('u_cbox_cnt_unrecomm').text
        print('name : %s | content : %s | like : %s | unlike : %s' % (name, content, like_count, unlike_count))


SCROLL_PAUSE_TIME = 1

driver = webdriver.Chrome('./chromedriver', options=set_headless_opt())
ssl._create_default_https_context = ssl._create_unverified_context
driver.get('https://m.post.naver.com/viewer/commentsView.nhn?volumeNo=17801142&memberNo=12466858#')

time.sleep(1)

btns = driver.find_elements_by_class_name('u_cbox_sort_option_wrap')
btns[1].click()
time.sleep(1)

move_to_scroll_down(driver.execute_script("return document.body.scrollHeight"))
next_btns = driver.find_elements_by_class_name('u_cbox_cnt_page')
is_not_end = True

while is_not_end:
    get_reply(driver.find_elements_by_class_name('u_cbox_area'))

    try:
        next_btns[2].click()
        time.sleep(2)

    except Exception as e:
        print(e)
        is_not_end = False
        driver.close()

driver.close()
