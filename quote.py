import requests
from bs4 import BeautifulSoup 


def getRandom():
    try:
        db = {"success":False, "data":[]}
        web= requests.get("http://www.quotationspage.com/random.php")
        soup = BeautifulSoup(web.content,'html.parser') 
        dataQuote =  dataAuthor = ""

        dataQuote = soup.find('dt', attrs = {'class','quote'})

        div_container = soup.find('dd', class_='author')  

        for tag in div_container.find_all('b'):
            for a in tag.find_all('a'):
                dataAuthor = a.text

        db["data"].append({"Quote" : dataQuote.text, "Author" : dataAuthor})
        db["success"] = True
        
        return db

    except Exception as e:
        db["error"] = str(e)
        return db




