# coding: utf-8

import requests
import json
import random
import MeCab

mt = MeCab.Tagger("-Ochasen")
mt.parse('')

def pedia(word):

    try:
        url = "http://ja.dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fja.dbpedia.org&query=prefix+dbp%3A+%3Chttp%3A%2F%2Fja.dbpedia.org%2Fresource%2F%3E%0D%0Aprefix+dbp-owl%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0Aprefix+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0A%0D%0ASELECT+*%0D%0AWHERE+%7B%0D%0A++++++++dbp%3A"+ word +"+dbp-owl%3AwikiPageWikiLink+%3Fthing1.%0D%0A++++++++%3Fthing1+rdfs%3Alabel+%3Fthing2.%0D%0A%7D%0D%0Alimit+250&should-sponge=&format=application%2Fsparql-results%2Bjson&timeout=0&debug=on"
        res = requests.get(url) 

        json_data = json.loads(res.text) 
    
        thesaurus = []
        for i,j in enumerate(json_data['results']['bindings']):
            thesaurus.append(json_data['results']['bindings'][i]['thing2']['value'])

        count = 0
        while True:
            part = thesaurus[random.randint(0,len(thesaurus)-1)]
            mb = mt.parse(part)
            count += 1

            if((u"固有名詞" not in mb) | (count > 100)):
                break

        return part
    
    except:

        return "エラー"

if __name__ == "__main__":

    while True:
        t = pedia("夏")
        text = mt.parse(t)
        if (u"固有名詞" not in text) & (u"月" not in text):
            break

    print(text)


