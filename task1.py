from bs4 import BeautifulSoup
import requests
import json

imbd_api = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
imbd_url = requests.get(imbd_api)
data = imbd_url.json
soup = BeautifulSoup(imbd_url.text,"html.parser")
div = soup.find("div",class_ = "lister")
body = div.find("tbody",class_ = "lister-list")
name = body.find_all("tr")


def scrape_top_list():
    main_list=[]
    dic={"position":"","name":"","year":"","rating":"","url":""}
    serial_number=1
    for i in name:
        movie = i.find("td",class_ = "titleColumn").a.get_text()
        year = i.find("td",class_="titleColumn").span.get_text()
        rating = i.find("td",class_="ratingColumn").strong.get_text()
        url = i.find("td", class_="titleColumn").a['href']
        dic["name"]=movie
        dic["year"]=int(year[1:5])
        dic["position"]=serial_number
        dic["rating"]=float(rating)
        dic["url"]="https://www.imdb.com"+url
        main_list.append(dic.copy())
        serial_number+=1
        with open("task1.json","w") as file:
            json.dump(main_list,file,indent=4)
    return(main_list)
scrape_top_list()


