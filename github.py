from selenium import webdriver
from time import sleep
import csv
import pandas as pd

browser = webdriver.Chrome()
browser.get("https://github.com/search?q=top+repositories")

for a in range(1,5):
    browser.execute_script('document.querySelector("#js-pjax-container > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.paginate-container.codesearch-pagination-container > div > a:nth-child('+str(a+2)+')").click();')
    sleep(0.5)
    
    content = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li')
    content = [x.text for x in content]
    #sleep(1)
    #browser.execute_script("document.querySelector('#js-pjax-container > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > ul > li:nth-child(1) > div.mt-n1 > div.f4.text-normal > a').click();")

    #c = [x.text for x in content]
    #document.querySelector("#js-pjax-container > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.paginate-container.codesearch-pagination-container > div > a:nth-child(3)")
    #document.querySelector("#js-pjax-container > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.paginate-container.codesearch-pagination-container > div > a:nth-child(4)")
    count = 1
    mat = []
    r = ['repository','description','language','ratings']
    mat.append(r)

    for i in content:
        row = []
        a = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li['+str(count)+']/div[1]/h3/a')
        a = [x.text for x in a]
        for j in a:
            row.append(j)
        b = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li['+str(count)+']/div[1]/p')
        b = [x.text for x in b]
        for j in b:
            row.append(j)
        c = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li['+str(count)+']/div[2]/div[1]')
        c = [x.text for x in c]
        for j in c:
            row.append(j)
        d = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li['+str(count)+']/div[2]/div[2]')
        d = [x.text for x in d]
        for j in d:
            row.append(j)
        mat.append(row)
        count += 1

    
s = pd.Series(mat)
print(s)

myFile = open('data.csv','w',newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(mat)
myFile.close()
browser.close()
browser.quit()

