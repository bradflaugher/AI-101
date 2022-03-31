#import the libraries you will use
import requests, bs4

#get the website
res = requests.get('http://www.digikey.com/product-search/en?keywords=MCP4018T-103E%2FLTTR-ND')
res.raise_for_status()

#this gets just the text for the website as a "soup" object
pageAsSoup = bs4.BeautifulSoup(res.text, "html.parser")

#we'll select the type of data that we want, this will be a list of "elements" aka
#text fields that match our selector.. if we wanted to figure out the type we could use
#the type(x) function where x is the thing you want to determine the type of
matchingElements = pageAsSoup.select('td[itemprop="description"]')

#if we got a result, print it's text, otherwise explain what we got
if(len(matchingElements)==1):
    print(matchingElements[0].getText())
elif(len(matchingElements)>1):
    print("I couldn't find a unique description")
elif(len(matchingElements)==0):
    print("I couldn't find a any description")
