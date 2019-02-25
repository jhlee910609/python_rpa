import ssl

from selenium import webdriver
import csv
import time
import urllib.request
from os import listdir, makedirs
from os.path import isdir
import os
import urllib

driver = webdriver.Chrome("./chromedriver")
base_url = 'https://twitter.com/'
# users = []

users = ["dktmfdl"]

base_path = '/Users/JunHee/Downloads/twitter_img'
SCROLL_PAUSE_TIME = 2
ssl._create_default_https_context = ssl._create_unverified_context


def getDir(targetDir):
    if not isdir(targetDir):
        makedirs(targetDir)


def moveToScrollDown(last_height):
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


def get_users():
    f = open('users_id.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for ele in rdr:
        users.append(str(ele).replace("[", "").replace("]", "").replace("'", ""))


# get_users()
for user in users:
    print(">>>>>>>>>>>>>> user id : " + user)
    out_dir = base_path + "/" + "@" + user
    getDir(out_dir)
    url = base_url + user + "/media"
    print(url)
    driver.get(url)

    time.sleep(2)
    moveToScrollDown(driver.execute_script("return document.body.scrollHeight"))
    # contents = driver.find_elements_by_class_name("js-original-tweet")

    photos = driver.find_elements_by_tag_name("img")
    for photo in photos:
        try:
            img_url = photo.get_attribute("src")
            splited_url = str(img_url).split("/")
            if (splited_url[3].__contains__('media')):
                save_url = out_dir + "/" + splited_url[-1]
                if not (os.path.isfile(save_url)):
                    print(img_url)
                    urllib.request.urlretrieve(img_url, out_dir + "/" + splited_url[-1])

        except Exception as e:
            print(e)
            pass

    print(">>>>>>>>>>>>>>>>>>>> end")

driver.quit()
print(">>>>>>>>>>> Process is completed!")
