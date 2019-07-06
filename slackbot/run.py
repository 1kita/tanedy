# coding: utf-8

import sys
import dbpedia
import scraping
import eliza
import requests
import random
import time
from slackbot.bot import Bot
from slackbot.bot import respond_to     
from slackbot.bot import listen_to      
from slackbot.bot import default_reply 

count = 0
saveword = ""

def main():
    bot = Bot()
    bot.run()

@default_reply()
def default_func(message):
    global count       
    global saveword

    text = ""
    text += message.body['text']    

    if(count == 0):
        msg = "テーマは何ですか？"
        count = 1
    elif(count == 1):
        word1 = dbpedia.pedia(text)
        word2 = scraping.relation(text)

        if(random.randint(0,1)): word = word1　else: word = word2 

        if(word != "エラー"):
            msg = word + "に馴染みはありますか？（はい/いいえ）"
        else:
            msg = "エラー"
        saveword = word
        count = 2

    elif((count == 2) & (text == "はい")):
        msg = "それはどういった事ですか？（行う/見る/行く/起こる/使う）"
        count = 3
    
    elif((count == 3) & (text in "行う見る行く起こる使う")):
        t = eliza.push(text)
        print(t["状況"][0])
        msg = saveword + t["状況"][random.randint(0,1)]
        count = 0

    else:
        msg = "テーマは何ですか？"
        count = 1
    

    message.reply(msg)    


if __name__ == "__main__":
    print('start slackbot')
    main()