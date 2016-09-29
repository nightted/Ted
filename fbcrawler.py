#-*- coding: utf-8 -*-
import requests
import json 
import jieba

TOKEN = "EAACEdEose0cBABlRtCJvRponmiL9chwJhIWSFlDZAS27TbFZA4iZA2Qzxfo31fMIXlITIDhDG2oDQmp5Srdg8zA1xWZBitfZA02z4WGaAmEmypLEp7ZAlz8uqXuCIOZCXbiDBdL16smq5bXrwkUSvRrapYGjByeD3PHLkwQWZBFXQAZDZD"

res = requests.get("https://graph.facebook.com/me/photos?limit=100&since=1420041600&access_token="+TOKEN)
jd = json.loads(res.text)


while "paging" in jd:
    for post in jd["data"]:
        print post
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    res = requests.get(jd["paging"]["next"]) #翻頁
    jd = json.loads(res.text)

    
def hatelikes(jd=jd):
    
    
    dic_g8 = {}
    dic_att = {}
    dic_percentage = {}


    while "paging" in jd :

        for post in jd["data"] : #當前此篇文章內容
            
            if "comments" in post  and "likes" in post :
                
                for people in post["comments"]["data"]:
                    #print (people["name"])
                    if len(people["from"]["name"]) and people["from"]["name"] not in [item['name'] for item in post["likes"]["data"]]:
                        
                        if people["from"]["name"] in dic_g8:
                            dic_g8[people["from"]["name"]] += 1
                            
                        else :
                            dic_g8[people["from"]["name"]] = 1
                    
                for people2 in post["likes"]["data"]:
                    
                    if people2["name"] in dic_att:
                        dic_att[people2["name"]] += 1
                    else :
                        dic_att[people2["name"]] = 1



                #print post 
                #print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                
        res = requests.get(jd["paging"]["next"]) #翻頁
        jd = json.loads(res.text)

        for name in dic_att:
            if dic_att.get(name) > 10:
                if name in dic_g8:
                    dic_percentage[name] = dic_g8.get(name)*100/(dic_g8.get(name)+dic_att.get(name))
                else :
                    dic_percentage[name] = 0

    return dic_percentage 




