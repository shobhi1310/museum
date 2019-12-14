from selenium import webdriver
from time import sleep
#import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import re


#data = {}
#data['Images'] = []
browser = webdriver.Chrome()
browser.get("http://www.nationalmuseumindia.gov.in")
#sleep(1)
browser.execute_script('document.querySelector("#close > img").click();')

content = browser.find_elements_by_xpath('//*[@id="ddsubmenu4"]/li')
content = [x.text for x in content]
#print(content)

mat=[]
for i in range(len(content)):
    if(i==6):
        continue
    browser.execute_script('document.querySelector("#ddsubmenu4 > li:nth-child('+str(i+1)+') > a").click();')
    #sleep(1)

    img = browser.find_elements_by_xpath('//*[@class="r-img"]')
    if(len(img)!=0):
        browser.execute_script('document.querySelector("#data > div:nth-child(3) > div.right-text > p > a").click();')
        for j in range(len(img)):
            dict = {}
            browser.execute_script('document.querySelector("#data > div:nth-child(4) > div:nth-child('+str(j+2)+') > a > img").click();')
            #sleep(2)
            url = browser.find_element_by_xpath('//*[@id="data"]/div[2]/div[1]/div/a/div/img').get_attribute('src')
            URL = browser.current_url
            r = requests.get(URL)
            soup = BeautifulSoup(r.content,'html5lib')
            content = soup.find_all('div',attrs={'class':'b-bold'})
            for x in content:
                c = x.find_all('p')
            name = browser.find_elements_by_xpath('//*[@id="data"]/div[2]/div[3]/strong')
            name = [x.text for x in name]
            tp = browser.find_elements_by_xpath('//*[@id="data"]/div[2]/div[3]/span')
            tp = [x.text for x in tp]
            for i in range(len(c)):
                a = c[i].find_all(text=True)
                m = []
                for l in a:
                    if(re.search('\w',l)):
                        m.append(l)
                if(len(m)==0):
                    continue
                else:
                    dict['place of origin'] = m[1]
                    break
            dict['url'] = url
            dict['name'] = name[0]
            dict['tp'] = tp[0]
            mat.append(dict)
with open('tp.json','w') as write_file:
    json.dump(mat,write_file,indent=4)

browser.close()
browser.quit()
