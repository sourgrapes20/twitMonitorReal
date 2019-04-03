import requests
from bs4 import BeautifulSoup as bs
import time
from urlGet import genHref
from twitterMonitor import twitMonitor

urlArray = ['https://twitter.com/ogBearlyWorking']
twitMonitor(urlArray)
