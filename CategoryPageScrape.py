from bs4 import BeautifulSoup
import requests
import json
import csv
import numpy as np
import pandas as pd
headers=["titles","details"]
with open('mycsvfile.csv','w') as g:
    w = csv.writer(g)
    w.writerow(headers)
response = requests.get('https://www.croma.com/computers-tablets/laptops/windows-laptops/c/855').text
soup = BeautifulSoup(response, 'html.parser')
links = soup.find_all('li', class_="product-item")
linksall=[]
#print(links)
for div in links:
    anchor=div.find('a')
    #print(anchor)
    if anchor==div.find('a'):
        link=anchor.get('href')
        linksall.append("https://croma.com"+link)
#print(linksall)
for page in range(1,len(linksall)):
    response = requests.get(linksall[page])
    if response.status_code != 200:	
        print("Error fetching page")
        exit()

    soupp = BeautifulSoup(response.content, 'html.parser')
    new_soup_cat=soupp.find_all('li', class_='cp-specification-spec-title')

    titles = []
    for i in new_soup_cat:
        i=str(i)
        j=i.replace('<h4>',' ')
        j=j.replace('</h4>',' ')
        j=j.replace('<li class="cp-specification-spec-title">',' ')
        j=j.replace('</li>',' ')
        j=j.strip()
        titles.append(j)
    new_soup_details=soupp.find_all('li', class_='cp-specification-spec-details')
    details = []
    for k in new_soup_details:
        k=str(k)
        l=k.replace('<h4>',' ')
        l=l.replace('</h4>',' ')
        l=l.replace('<li class="cp-specification-spec-details">',' ')
        l=l.replace('</li>',' ')
        l=l.replace('<a class="brand-url-pdp spec-brand-url" href="/croma-store/b/b-0082" rel="noopener noreferrer" target="_blank">',' ')
        l=l.replace('</a>',' ')
        l=l.strip()
        details.append(l)
    final = {}
    for key in titles:
        for value in details:
            final[key]=value
            details.remove(value)
            break
    with open('mycsvfile.csv','a') as f:
        w = csv.writer(f)
        w.writerow(final.keys())
        w.writerow(final.values())
        w.writerow("\n")

_mat=pd.read_csv("mycsvfile.csv")
_mat=_mat[_mat.columns].values
_t_mat=np.transpose(_mat)
print(_t_mat)