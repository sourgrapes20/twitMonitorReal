import requests
from bs4 import BeautifulSoup as bs
import time
from urlGet import genHref
import cv2
import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

userName = 'ogBearlyWorking'
url = 'https://twitter.com/'+userName

r = requests.get(url)
soup = bs(r.text,'html.parser')
#print(soup)

def twitMonitor(url):
    counter = 0
    isRunning = True
    unsortedTweetsEven = []
    unsortedTweetsOdd = []
    k = cv2.waitKey(1) & 0xFF
    # press 'q' to exit
    while isRunning==True:
        if counter==0:
            print("We are a go!\n")
        if counter%2==0:
            r = requests.get(url)
            soup = bs(r.text,'html.parser')
            unsortedTweetsEven.clear()
            for hit in soup.findAll(attrs={'class':'js-tweet-text-container'}):
                unsortedTweetsEven.append(hit.text)
            #print("Even: " + unsortedTweetsEven[0])
        else:
            r = requests.get(url)
            soup = bs(r.text,'html.parser')
            unsortedTweetsOdd.clear()
            for hit in soup.findAll(attrs={'class':'js-tweet-text-container'}):
                unsortedTweetsOdd.append(hit.text)
            #print("Odd: " + unsortedTweetsOdd[0])
        counter = counter+1
        if counter>1:
            if(unsortedTweetsOdd!=unsortedTweetsEven):
                hrefValue = genHref(url)
                link = 'https://twitter.com/' + hrefValue
                if counter%2==0:
                    print(link,unsortedTweetsOdd[0],datetime.datetime.now())
                    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/562741095272939547/5iQrjyaghQLo44wYosGT-gQQueF9LU0QbdVvn7Nq7cjU1Y_nY-TuN52qDEzdkwqZhwI5')
                    embed = DiscordEmbed(title=userName, description=unsortedTweetsOdd[0], color=0000000)
                    webhook.add_embed(embed)
                    webhook.execute()
                else:
                    print(link,unsortedTweetsEven[0],datetime.datetime.now())
                    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/562741095272939547/5iQrjyaghQLo44wYosGT-gQQueF9LU0QbdVvn7Nq7cjU1Y_nY-TuN52qDEzdkwqZhwI5')
                    embed = DiscordEmbed(title=userName, description=unsortedTweetsEven[0], color=0000000)
                    webhook.add_embed(embed)
                    webhook.execute()


twitMonitor(url)
