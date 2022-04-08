import urllib.request
from bs4 import BeautifulSoup
import requests

def urlArrFromSite(url):

    urlArr = []
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    mainText = soup.find('div',attrs={"class":"mw-body-content mw-content-ltr"})
    aBlocks = mainText.findAll('a',attrs={"href":not None})
    
    for aBlock in aBlocks:
        href = aBlock['href']
        if(href.startswith("/wiki") and not href.endswith("jpg")):
           urlArr.append("https://en.wikipedia.org" + href)
    return(urlArr)

def isUChiFromURL(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    infoBioCard = soup.find('table',attrs={"class":"infobox biography vcard"})
    infoCard = soup.find('table',attrs={"class":"infobox vcard"})
    if(infoBioCard is not None):
        if("University of Chicago" in infoBioCard.text):
            print(url)
    if(infoCard is not None):
        if("University of Chicago" in infoCard.text):
            print(url)
            
url ='https://en.wikipedia.org/wiki/List_of_people_on_the_postage_stamps_of_the_United_States'
urlArr = urlArrFromSite(url)
print(str(len(urlArr)) + " links to check")
for link in urlArr:
    isUChiFromURL(link)
print('Done')
