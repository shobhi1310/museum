from selenium import webdriver
from time import sleep
import pandas as pd
import csv

browser = webdriver.Chrome()

browser.get("http://intranet.iittp.ac.in")
#sleep(0.5)
mat = []
mat.append(['Roll number','Name','Email'])
for i in range(2,5):
    browser.execute_script('document.querySelector("#mm-17 > li:nth-child('+str(i+1)+') > a").click()')
    #sleep(0.5)
    for j in range(0,4):
        #sleep(0.5)
        browser.execute_script('document.querySelector("#yt_component > article > div.yt-tabs.style-oranges.vertical > ul > li:nth-child('+str(j+1)+') > a").click();')
        nr = browser.find_elements_by_xpath('//*[@id="example"]/tbody/tr')
        nr = [x.text for x in nr]
        count = 2
        for a in nr:
            if(a!=''):
                for c in range(3):
                    row = browser.find_elements_by_xpath('//*[@id="example"]/tbody/tr['+str(count)+']/td')
                    row = [x.text for x in row]
                #print(row)
                count += 1
                r = []
                for b in row:
                    if(b!=''):
                        r.append(b)
                mat.append(r)

s = pd.Series(mat)
print(s)
'''
myfile = open('data.csv','w',newline='')
with myfile:
    writer = csv.writer(myfile)
    writer.writerows(mat)
myfile.close()
'''
#sleep(0.5)
browser.close()
browser.quit()
