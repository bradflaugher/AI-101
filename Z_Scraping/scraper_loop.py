#import the libraries you will use
import requests, bs4

urls = [''] * 3
urls[0] = 'http://www.digikey.com/product-search/en?keywords=MCP4018T-103E%2FLTTR-ND'
urls[1] = 'http://www.digikey.com/product-detail/en/maxim-integrated/MAX5422ETA%2BT/MAX5422ETA%2BTDKR-ND/2425813'
urls[2] = 'http://www.digikey.com/product-detail/en/maxim-integrated/MAX5481EUD%2B/MAX5481EUD%2B-ND/1779810'

for url in urls:
    #get the website
    res = requests.get(url)
    res.raise_for_status()

    #this gets just the text for the website as a "soup" object
    page_as_soup = bs4.BeautifulSoup(res.text, 'html.parser')

    #we'll select the type of data that we want, this will be a list of "elements" aka
    #text fields that match our selector.. if we wanted to figure out the type we could use
    #the type(x) function where x is the thing you want to determine the type of
    matching_descriptions = page_as_soup.select('td[itemprop="description"]')
    matching_qtys_available = page_as_soup.select('td[id="quantityAvailable"]')
    

    #if we got a result, save its text, otherwise explain say we haven't found anything
    if(len(matching_descriptions)==1):
        matching_description_text = (matching_descriptions[0].getText()).replace('\n',' ').replace('  ','')
    else:
        matching_description_text = 'Not Found'
        
    if(len(matching_qtys_available)==1):
        matching_qty_available_text = (matching_qtys_available[0].getText()).replace('\n',' ').replace('  ','')
    else:
        matching_qty_available_text = 'Not Found'
    

    #write to our file, for more info check out https://docs.python.org/2/tutorial/inputoutput.html
    f = open('output.csv','a')
    f.write('%s,%s,%s\n' % (url,matching_description_text,matching_qty_available_text))
    