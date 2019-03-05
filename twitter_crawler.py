import ssl

from selenium import webdriver
import csv
import urllib.request
from os import listdir, makedirs
from os.path import isdir
import os
import urllib
import time



def set_headless_opt():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    return options



def make_folder(target_dir):
    if not isdir(target_dir):
        makedirs(target_dir)


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


def get_users():
    f = open('users_id.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for ele in rdr:
        users.append(str(ele).replace("[", "").replace("]", "").replace("'", ""))


def open_date():
    f = open(out_dir + "/date.csv", 'r', encoding='utf-8')
    return f.readline()


def write_date(date):
    f = open(out_dir + "/date.csv", "w", encoding='utf-8', newline='')
    f.write(date)

driver = webdriver.Chrome("./chromedriver", options=set_headless_opt())
base_url = 'https://twitter.com/'
# users = []

users = ["EIMI_FUKADA"]

base_path = '/Users/JunHee/Downloads/twitter_img'
SCROLL_PAUSE_TIME = 2
ssl._create_default_https_context = ssl._create_unverified_context


start_time = time.time()
# get_users()
total_user = len(users)
user_count = 1
for user in users:
    out_dir = base_path + "/" + "@" + user
    url = base_url + user + "/media"
    make_folder(out_dir)
    driver.get(url)

    time.sleep(2)

    try :
        latest_date = driver.find_element_by_class_name("_timestamp").get_attribute("data-time-ms")
    except Exception as e:
        print("There is no account")
        continue

    print(">>>>>>>>>>>>>> user id : %s, %d of %d" % (user, user_count, total_user))
    user_count += 1

    if (os.path.isfile(out_dir + "/date.csv")):
        if (open_date() == latest_date):
            print("already updated!")
            continue
    else:
        write_date(latest_date)

    move_to_scroll_down(driver.execute_script("return document.body.scrollHeight"))
    print(url)

    contents = driver.find_elements_by_class_name("js-original-tweet")

    for content in contents:

        photos = content.find_elements_by_tag_name("img")

        for photo in photos:
            try:
                img_url = photo.get_attribute("src")
                splited_url = str(img_url).split("/")

                if (splited_url[3].__contains__('media')):
                    save_url = out_dir + "/" + splited_url[-1]

                    if not (os.path.isfile(save_url)):
                        urllib.request.urlretrieve(img_url, out_dir + "/" + splited_url[-1])

            except Exception as e:
                print(e)
                pass
    print(">>>>>>>>>>>>>>>>>>>> end")

driver.quit()
print(">>>>>>>>>>>>>>>>>>>> All photo is downloaded!")
print("duration : %d" % (time.time() - start_time))
