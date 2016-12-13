# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:26:37 2016

Modified by Guo Yao
"""

import sys
from pprint import pprint
from random import choice
import os
 
EOS = ['.', '?', '!']
 
 
def build_dict(words,n):
    """
    Build a dictionary from the words.
 
    (word1, word2) => [w1, w2, ...]  # key: tuple; value: list
    """
    d = {}
    
    for i, word in enumerate(words):
        prior=[]
        try:
            for j in range(n+1):
                prior.append(words[i+j])
#            first, second, third = words[i], words[i+1], words[i+2]
        except IndexError:
            break
        key = tuple(prior[:n])
        if key not in d:
            d[key] = []
        d[key].append(prior[n])
    return d
 
 
def generate_sentence(d,n):
    li = [key for key in d.keys() if key[0][0].isupper()]
    key = choice(li)
#    key=('It','is')
    li = []
    start=key[0]
    middle=key[-(n-1):]
    prior = list(key)
    li.extend(prior)
    while True:
        try:
            final = choice(d[key])
        except KeyError:
            break
        li.append(final)
        if final[-1] in EOS:
            break
        # else
        tmp=list(middle)
        tmp.append(final)
        key = tuple(tmp)
        middle=key[-(n-1):]
#        key = (second, third)
        
#        first, second = key
 
    return ' '.join(li)
 
 

 
####################
if __name__ == "__main__":
#    path="./Experiment/data/Romantic"
#    pathDir=os.listdir(path)
#    text=str()
#    for allDir in pathDir:
#        child=os.path.join('%s%s' % (path+'/', allDir))
#        with open(child,'rt',encoding="utf-8") as f:
#            text +=f.read()
    with open("examples.txt",'rt',encoding='gbk') as f:
        text=f.read()
    words = text.split()
    print(words)
    n=2
    d = build_dict(words,n)
    pprint(d)
    print()
    txt=str()
    for i in range(10):
        sent = generate_sentence(d,n)
        txt+=sent
    print(txt)
#    if sent in text:
#        print('# existing sentence :(')
