import requests
from bs4 import BeautifulSoup as bs
import time

userName = 'ogBearlyWorking'
url = 'https://twitter.com/'+userName

def genHref(url):
    r = requests.get(url)
    soup = bs(r.text,'html.parser')
    #print(soup)
    tweetHTML = soup.find_all(attrs={"class":"tweet-timestamp js-permalink js-nav js-tooltip" })
    #print(tweetHTML)
    recentHrefValue = tweetHTML[0]['href']
    #print(recentHrefValue)
    return recentHrefValue

genHref(url)
