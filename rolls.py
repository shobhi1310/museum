from time import sleep
import csv
import pandas as pd
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://intranet.iittp.ac.in/index.php")

mat = []
mat.append(['Roll No','Name','Email'])
#c = browser.find_elements_by_tag_name('iframe')
#c = [x.text for x in c]
#print(c)
browser.execute_script("document.querySelector('#mm-17 > li:nth-child(2) > a').click();")
sleep(1)
browser.find_element_by_xpath("//*[@id='yt_component']/article/div[2]/ul/li[2]/a").click()

#browser.execute_script("document.querySelector('#yt_component > article > div.yt-tabs.style-oranges.vertical > ul > li:nth-child(2) > a').click();")

'''
for a in range(5):
    #sleep(1)
    browser.execute_script("document.querySelector('#mm-17 > li:nth-child("+str(a+1)+") > a').click();")
    #sleep(0.5)
    #browser.execute_script("document.querySelector('#yt_component > article > div.yt-tabs.style-oranges.vertical > ul > li:nth-child(1) > a').click();")
    '''
'''
    for b in range(5):
        sleep(1)
        r = browser.find_elements_by_xpath("/html/body/div[2]/div[1]/section[2]/div/div/div/div/div[2]/article/div[2]/div/div["+str(b+1)+"]/table/tbody/tr")

        #rows = []
        #columns = []

        count = 2
        #mat = []

        for i in r:
            if(i.text==''):
                break
            else:
                rows = []
                c = browser.find_elements_by_xpath('/html/body/div[2]/div[1]/section[2]/div/div/div/div/div[2]/article/div[2]/div/div['+str(b+1)+']/table/tbody/tr['+str(count)+']/td')
                count += 1
                for j in c:
                    if(j.text!=''):
                        rows.append(j.text)
                #print(rows)
                #print('\n')
                mat.append(rows)
        #sleep(1)
'''
'''
s = pd.Series(mat)
print(s)
browser.close()
browser.quit()
'''
'''
myfile = open('data.csv','w',newline='')
with myfile:
    writer = csv.writer(myfile)
    writer.writerows(mat)
'''
