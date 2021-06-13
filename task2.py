from task1 import scrape_top_list
import json
import pprint

scrapped=scrape_top_list()
def group_by_year(movies):
    years = []
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[] for i in years }
    for i in movies:
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
                with open("task2.json","w") as file:
                    json.dump(movie_dict,file,indent=4)
    return movie_dict
# pprint.pprint(movie_dict)
group_by_year(scrapped)



# from task1 import scrape_top_list
# import pprint
# import json
# def movies_by_year():
#         s_m = scrape_top_list()
#         movies_year_list = []
#         for i in s_m:
#                 year=i["year"]
#                 if year not in movies_year_list:
#                         movies_year_list.append(year)
#         movies_year_dic={}
#         for i in movies_year_list:
#                 movies_year_dic.update({i:[]})
#         # print(movies_year_dic)
#         c = 1
#         for j in s_m:
#                 year = j["year"]
#                 # print(c,year)
#                 c+=1
#                 for k in movies_year_dic:
#                         if k == year:
#                                 movies_year_dic[k].append(j)
#                                 with open("p.json","w") as file:
#                                     json.dump(movies_year_dic,file,indent=4)
#         return(movies_year_dic)
# pprint.pprint(movies_by_year())




