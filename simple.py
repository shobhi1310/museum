from selenium import webdriver
import pandas as pd

browser = webdriver.Chrome()
browser.get("https://www.python.org/")

full_page = browser.find_elements_by_xpath("//div")
elements = [x.text for x in full_page]

#elements = [1,3,4,5]

s = pd.Series(elements)

print(elements,'\n')

##print(s)
