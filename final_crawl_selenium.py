from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

class Crawler(object):
 def crawl_data(self):
  chrome_options = Options()
  chrome_options.add_argument("--window-size=1920,1080")
  # Using the crome driver file path
  driver = webdriver.Chrome('/Users/SharadAggrawal/Downloads/chromedriver', chrome_options=chrome_options)  # Optional argument, if not
  driver.get('http://elplclab01.cern.ch/index.htm')
  sleep(30)
  print driver.page_source
  #print driver.title
  #driver.save_screenshot('/Users/SharadAggrawal/Desktop/web_scrapping_selenium/test.png')
  driver.quit()

if __name__ == "__main__":
 crawl = Crawler()
 crawl.crawl_data();


##converting driver result to BS and using it through html parser
# result = driver.find_element_by_class_name('profile-col-main')
# htmlText =  result.get_attribute('innerHTML')
# Here we  initialized the beautiful soup to extract data from the html
# bs = BeautifulSoup(res.text, 'html.parser')
# ele = bs.select_one('.profile-props')
# currency = ele.select('.propblock-body')
# Here we printing the crawled data
# print currency[2].get_text(strip=True)
# print currency[3].get_text(strip=True)
# print currency[4].get_text(strip=True)
# print bs
#print driver.find_element_by_tag_name('body')
