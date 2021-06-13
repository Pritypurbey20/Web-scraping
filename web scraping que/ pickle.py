from bs4 import BeautifulSoup
import requests
import json
import pprint

api = "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
url = requests.get(api)
soup = BeautifulSoup(url.text,"html.parser")
page_div=soup.find("div",class_="_1gX7")
product_no=page_div.span.get_text()
splited_list=product_no.split(" ")
a=int(splited_list[1])
b=a//32+1
Pickle = []
Serial_number=1
j=1
while j<=b:
    Api="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(j)
    Url=requests.get(Api)
    Soup = BeautifulSoup(url.text,"html.parser")
    div = Soup.find("div",class_="_3RA-")
    div1 = div.find_all("div",class_="UGUy")
    sdiv = div.find_all("div",class_="_1kMS")
    tdiv = div.find_all("div",class_="_3WhJ")
    i=0
    while i<len(div1):
        Pickle_name=div1[i].get_text()
        Pickle_price=sdiv[i].get_text()
        Pickle_link=tdiv[i].a["href"]
        Url="https://paytmmall.com/"+Pickle_link
        dict={"Name":"","Price":"","Url":"","Position":""}
        dict["Name"]=Pickle_name
        dict["Price"]=Pickle_price
        dict["Url"]=Url
        dict["Position"]=Serial_number
        Pickle.append(dict.copy())
        Serial_number+=1
        i+=1
    j+=1
with open("pickle.json","w") as file:
    json.dump(Pickle,file,indent=4)
