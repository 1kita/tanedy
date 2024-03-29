# coding: utf-8

def push(word):
    gPats = {
        "行う":{
            "実行":"しますか",
            "同伴":"を誰としますか?",
            "状況":{
                0:"をしていて、困ったことはありましたか?",
                1:"をしていて、嬉しかったことはありましたか?"
            }
        },
        "見る":{
            "実行":"を見ましたか?",
            "同伴":"誰と見ましたか?",
            "状況":{
                0:"を見ていて、困ったことはありましたか?",
                1:"をしていて、嬉しかったことはありましたか?"
            }
        },
        "行く":{
            "実行":"に行きましたか?",
            "同伴":"へ誰と行きましたか?",
            "状況":{
                0:"に行っていて、困ったことはありましたか?",
                1:"に行っていて、嬉しかったことはありましたか?"
            }
        },
        "起こる":{
            "実行":"が実際に起きたことはありますか?",
            "同伴":"が起きた時に、誰かと一種にいましたか?",
            "状況":{
                0:"が起きた時、困ったことはありましたか?",
                1:"が起きた時、困ったことはありましたか?"
            }
        },
        "使う":{
            "実行":"が実際に起きたことはありますか?",
            "同伴":"が起きた時に、誰かと一種にいましたか?",
            "状況":{
                0:"を使っていて、困ったことはありましたか?",
                1:"を使っていて、不便だと思うことはありましたか?"
            }
        }
    }

    part = gPats.get(word)

    return part

if __name__ == "__main__":
    t = push("行う")
    print(t["状況"][0])