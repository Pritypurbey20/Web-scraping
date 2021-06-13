from bs4 import BeautifulSoup
import requests
import json

api = "https://webscraper.io/test-sites"
url = requests.get(api)
data = url.json
soup = BeautifulSoup(url.text,"html.parser")
data_list=[]
link=soup.find_all("h2")
Position=1
for i in link:
    Link=i.find("a")["href"]
    Name=i.find("a").get_text().strip()
    dict={"Position":"","Name":"","Link":""}
    dict["Position"]=Position
    dict["Name"]=Name
    dict["Link"]=Link
    data_list.append(dict.copy())
    Position+=1
with open("Ecommerce.json","w") as file:
    json.dump(data_list,file,indent=4) 




