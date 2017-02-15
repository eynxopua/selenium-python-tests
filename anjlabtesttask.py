from selenium import webdriver
from faker import Factory # for generating fake data
from selenium.common.exceptions import NoSuchElementException
import sys

driver = webdriver.Chrome()
driver.get("http://anjlab.com/en/")
driver.maximize_window()

try:
    show_search = driver.find_element_by_class_name('icon-minti-search')
    show_search.click()
except NoSuchElementException:
    print('Failed, Can\'t find search button')
    driver.close()
    sys.exit(0)

search = driver.find_element_by_name('s')
search.send_keys('offgrid')
search.submit()


try:
    offgrid = driver.find_element_by_xpath('//*[@title="Permalink to Off.Grid:Electric Surge"]')
    offgrid.click()
except NoSuchElementException:
    print('Failed, Can\'t find Offgrid link')
    driver.close()
    sys.exit(0)
try:
    hire = driver.find_element_by_id('menu-item-1574')
    hire.click()
except NoSuchElementException:
    print('Failed, Can\'t find hiring menu button')
    driver.close()
    sys.exit(0)

try:
    ruby_developer = driver.find_element_by_xpath('//a[@href="http://anjlab.com/ru/hire/vakansiya-rails-razrabotchik/"]')
    ruby_developer.click()
except NoSuchElementException:
    print('Failed, Can\'t find ruby developer link')
    driver.close()
    sys.exit(0)

try:
    request_button = driver.find_element_by_xpath('//a[@href="/hire#hire-form"]')
    request_button.click()
except NoSuchElementException:
    print('Failed, Can\'t find form opening button')
    driver.close()
    sys.exit(0)


# form-filling
try:
    name = driver.find_element_by_name('your-name')
    mail = driver.find_element_by_name('your-email')
    position = driver.find_element_by_name('your-position')
    about = driver.find_element_by_name('your-message')
    cv = driver.find_element_by_name('file-161')
except NoSuchElementException:
    print('Failed, Can\'t find one of inputs in submission form')
    driver.close()
    sys.exit(0)

fake = Factory.create()

cv_file = open("cv.txt", "w+")
cv_file.write(fake.text())
cv_file.close()

name.send_keys(fake.name())
mail.send_keys(fake.email())
position.send_keys(fake.job())
about.send_keys(fake.text())
cv.send_keys("/path/to/the/created/cv/txt/file")

driver.close()
print('Test Passed')
sys.exit(0)