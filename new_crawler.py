from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get("https://www.naver.com/")
    keyword = input("키워드를 입력하세요 : ")
    element = driver.find_element_by_id('query')
    element.send_keys(keyword)
    element.send_keys(Keys.RETURN)

    div = driver.find_element_by_class_name('_blogBase')
    blogs = div.find_elements_by_xpath('./ul/li')
    for blog in blogs:
        title_tag = blog.find_element_by_class_name('sh_blog_title')
        print(title_tag.get_attribute('title'))
        print(title_tag.get_attribute('href'))

except Exception as e:
    print(e)

    # driver.quit()