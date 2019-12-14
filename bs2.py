import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import re

browser=webdriver.Chrome()
browser.get("http://gcu.iittp.ac.in/home")

URL = browser.current_url
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')

print(soup)
