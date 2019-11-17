from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC

try:
    DRIVER = webdriver.Firefox()
except WebDriverException:
    DRIVER = webdriver.Chrome()

ELEMENT = DRIVER.find_element_by_tag_name("body")

with open("selenium_reference.xml", "w") as fh:
    fh.write("driver ({}) methods\n".format(type(DRIVER)))
    fh.write("---------------------\n")
    for each in dir(DRIVER):
        fh.write(each)
        fh.write('\n')

    fh.write("\n\nwebElement ({}) methods\n".format(type(ELEMENT)))
    fh.write("---------------------\n")
    for each in dir(ELEMENT):
        fh.write(each)
        fh.write('\n')

    fh.write("\n\nWebDriverWait ({}) methods\n".format(type(WebDriverWait)))
    fh.write("---------------------\n")
    for each in dir(WebDriverWait):
        fh.write(each)
        fh.write('\n')

    fh.write("\n\nexpected_conditions ({}) methods\n".format(type(EC)))
    fh.write("---------------------\n")
    for each in dir(EC):
        fh.write(each)
        fh.write('\n')
