import requests
from bs4 import BeautifulSoup

def scrape(URL):
    
    response=requests.get(URL)
    soup=BeautifulSoup(response.text,"lxml")

    print("The response is...",soup.text)
    
    quotes=soup.find_all("div", class_="field-content")
    
    for quote in quotes:
        quote_txt=quote.find("p").get_text()
        print("Quote: ",quote_txt)
        
        author=quote.find("small",class_="author").get_text()
        print("Author: ",author)
        
        all_tags=quote.find_all("a",class_="tag")
        tags=[]
        
        for tag in all_tags:
            value=tag.get_text()
            tags.append(value)
        
        print("The tags are..",tags)


URL="https://www.uwindsor.ca/dailynews/all-news"

scrape(URL)

#for page_no in range(2,21):
 #   URL=f"https://quotes.toscrape.com/page/{page_no}"
  #  scrape(URL)