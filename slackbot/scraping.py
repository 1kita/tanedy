# coding: utf-8

import requests
from bs4 import BeautifulSoup
import random

def relation(word):
    w = ""
    try:
        try:
            target_url = "https://contentsearch.jp/textmining.php?q="+word+"&mode=highreactiononly&authority="
            r = requests.get(target_url)         
            soup = BeautifulSoup(r.text,"html.parser") 
            tr = soup.find_all('tr')[0]
            text = []
            for a in tr.find_all('td')[0]:
                text.append(a.get_text())

            num = round(len(text)-1/2)
            text = text[0:num]
            w = text[random.randint(0,len(text)-1)]

        except:
            target_url = "https://www.google.com/trends/correlate/search?e="+ word +"&t=monthly&p=jp#default,90"
            r = requests.get(target_url)         
            soup = BeautifulSoup(r.text,"html.parser") 
            # print(soup)
            li = soup.find_all('li',{"class":"result"})
            atug = []
            for a in li:
                atug += a.find_all('a')

            # print(atug)
            text = []
            for a in atug:
                text.append(a.get_text())

            # print(text)

            num = round(len(text)-1/2)
            text = text[0:num]
            w = text[random.randint(0,len(text)-1)]
            w = w.lstrip(word)
    except :
        w = "エラー"

    return  w
   

if __name__ == "__main__":
    t = relation("夏")
    print(t)