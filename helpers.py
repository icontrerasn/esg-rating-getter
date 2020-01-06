import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def search_company(keyword):
    search_url = 'https://www.msci.com/esg-ratings?p_p_id=esgratingsprofile&' \
        'p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=searchEsgRatingsProfiles&' \
        'p_p_cacheability=cacheLevelPage&_esgratingsprofile_keywords={}'.format(keyword)
    search_response = requests.get(search_url)
    search_json = search_response.json()
    # We get the first result, since it is the best match for the searched term
    result = search_json[0]
    print(result)
    company_data = {
        'id': result['url'],
        'name': result['encodedTitle']
    }
    return company_data

def get_rating(company_data):
    company_url = 'https://www.msci.com/esg-ratings/issuer/{name}/{id}'.format(**company_data)
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(company_url)
    # Execute script to scroll down the page and make sure that we are loading the full page
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;')
    # Sleep for 5s to load whole page
    time.sleep(5)
    element = driver.find_element_by_class_name('ratingdata-company-rating')
    element_classes = element.get_attribute('class').split()
    # print(element_classes)

# company_data = search_company('latam')
# get_rating(company_data)