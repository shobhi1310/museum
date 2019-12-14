import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import re

browser=webdriver.Chrome()
browser.get("http://www.nationalmuseumindia.gov.in/prodCollections.asp?pid=80&id=8&lk=dp8")

URL = browser.current_url
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')

content = soup.find_all('div',attrs={'class':'b-bold'})

for x in content:
    c = x.find_all('p')

#print(type(c))
#blacklist = [
#    '\n\t',
#]
a = c[0].find_all(text=True)
m = []
print(a)
for l in a:
    if(re.search('\w',l)):
        m.append(l)
if(len(m)!=0):
    print(m)
    dict['place of origin'] = m[1]
#print(len(m))

url = browser.find_element_by_xpath('//*[@id="data"]/div[2]/div[1]/div/a/div/img').get_attribute('src')
dict = {}
dict['url'] = url
#dict['pls'] = m[1]
#for i in range(0,7,2):
#    dict[m[i]] = m[i+1]

y = json.dumps(dict,indent=4)
print(y)
browser.close()
browser.quit()
#for i in range(len(c)):
#    if (i==1):
#        a = c[i].find_all('strong')

#print(a)
