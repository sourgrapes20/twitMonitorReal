from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
#url = 'https://www.footlocker.com/product/Jordan-Retro-1-High-OG---Men-s/55088160.html'
url = input("Enter the url to check stock on: ")


sizeHTML = []
allSizes = []
sizesInStock = []
sizesInStock2 = []
counter = 0
isRunning = True
while isRunning == True:
    session = HTMLSession()
    r = session.get(url)
    soup = bs(r.text, "html.parser")
    for hit in soup.findAll(attrs={'class' : 'c-form-label-content'}):
        sizeHTML.append(hit.text)
    #trimming down to just sizes
    for i in range(len(sizeHTML)):
        if len(sizeHTML[i])!=0:
            allSizes.append(sizeHTML[i])
    #print(allSizes)
    for i in range(len(allSizes)):
        sizeToCheck = allSizes[i]
        options = soup.find_all("input",{"aria-label":"Size " + sizeToCheck})
        if(len(options)==0):
            print(sizeToCheck + " is out of stock for " + url)
        else:
            if counter%2==0:
                sizesInStock.append(sizeToCheck)
                print("Check1")
            else:
                sizesInStock2.append(sizeToCheck)
                print("Check2")
            #print(sizeToCheck + " is in stock for " + url)
    #print(sizesInStock)
    #print(sizesInStock2)
    counter = counter+1
