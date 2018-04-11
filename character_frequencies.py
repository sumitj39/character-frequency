#coding: UTF-8
import re
from collections import Counter
import operator
othu = u"ಾಿೀುೂೃೄೆೇೈೊೋೌ್ಂಃ"

def filter_kan_chars(text):
    return ''.join(list(filter(lambda x:x>='\u0c80' and x<='\u0cff',list(text))))

def count(cobj, txt):
    txt = filter_kan_chars(txt)
    replstr = re.sub("|".join(othu),"",txt)
    cobj.update(replstr)

#0C80 0CFF
if __name__ == '__main__':
    print("\n")
    cobj = Counter()
    with open("kannada-text", encoding="utf-8") as f:
        count(cobj, f.read())
    
    total  = sum(x for x in cobj.values())
    for count,(char, freq) in enumerate(sorted(cobj.items(),key=operator.itemgetter(1), reverse=True), 1):
        print("{0:2} : {1:<4}({2:<5.2f}%)".format(char, freq,100*freq/total), end = "\t")
        if count%4 == 0:
            print("\n")
    print("\n")


