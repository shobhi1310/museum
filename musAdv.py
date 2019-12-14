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
            browser.execute_script('document.querySelector("#data > div:nth-child(4) > div:nth-child('+str(j+2)+') > a > img").click();')
            url = browser.find_element_by_xpath('//*[@id="data"]/div[2]/div[1]/div/a/div/img').get_attribute('src')
            sleep(2)
            URL = browser.current_url
            r = requests.get(URL)

            soup = BeautifulSoup(r.content,'html5lib')

            content = soup.find_all('div',attrs={'class':'b-bold'})
            for x in content:
                c = x.find_all('p')

            for j in range(len(c)):
                a = c[j].find_all(text=True)
                if(len(a)==0):
                    continue
                else:
                    m = []
                    for i in a:
                        if ((re.search('\w',i))):
                            m.append(i)
                    dict = {}
                    dict['url'] = url
                    for i in range(0,7,2):
                        dict[m[i]] = m[i+1]
                    print(dict)
                    mat.append(dict)
                    break

s = json.dumps(mat,indent=4)
print(s)
#print(mat)

#sleep(1)
browser.close()
browser.quit()
#print(images)

#browser.close()
