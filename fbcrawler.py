#-*- coding: utf-8 -*-
import requests
import json 
import jieba
import operator

TOKEN = "EAACEdEose0cBAB1ZBqekistK6wcvZAa56VjCNk1MlNFC07zIk1rQWbrLBxlVlwK8panNaqJG78PpO9d74KVb1bhgynHq66iKMa5ZASknQnzHHplv6JMF9d6V5d0kU8zUAUfTB2Mh450x35BEb6egp83XqSEe19AKVNI4mMHQAZDZD"

res = requests.get("https://graph.facebook.com/me/posts?limit=100&since=1251561600&access_token="+TOKEN)
jd = json.loads(res.text)

'''
while "paging" in jd:
    for post in jd["data"]:
        print post
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    res = requests.get(jd["paging"]["next"]) #翻頁
    jd = json.loads(res.text)
'''
    
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

sorted_rank = sorted(hatelikes().items() , key = operator.itemgetter(1),reverse = True)

for ele in sorted_rank:
    print ele[0] , ele[1] ,'%'




