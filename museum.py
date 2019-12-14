from selenium import webdriver
from time import sleep
import pandas as pd


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
    browser.execute_script('document.querySelector("#ddsubmenu4 > li:nth-child('+str(i+1)+') > a").click();')
    #sleep(1)

    img = browser.find_elements_by_xpath('//*[@class="r-img"]')
    if(len(img)!=0):
        browser.execute_script('document.querySelector("#data > div:nth-child(3) > div.right-text > p > a").click();')
        for j in range(len(img)):
            browser.execute_script('document.querySelector("#data > div:nth-child(4) > div:nth-child('+str(j+2)+') > a > img").click();')
                                    #document.querySelector("#data > div:nth-child(4) > div:nth-child(2) > a > img")
                                    #document.querySelector("#data > div:nth-child(4) > div:nth-child(3) > a > img")
            topic = browser.find_elements_by_xpath('//*[@id="data"]/div[2]/div[5]/p[2]')
                                                    #//*[@id="data"]/div[2]/div[5]/p[2]/strong[1] for the type info
                                                    #//*[@id="data"]/div[2]/div[5]/p[2]/text()[1] for the description
            topic = [x.text for x in topic]
            print(topic)
            mat.append(topic)

s = pd.Series(mat)
print(mat)

#sleep(1)
browser.close()
browser.quit()
#print(images)

#browser.close()
