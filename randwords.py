#!/bin/python3

# Developer : Hamdy Abou El Anein

import random

words=[]
user=""

user = input("\n\n\nEntrez votre nom ici : ")

def dictio():
    with open('listfr.txt') as f:
        #words = f.read().split(' ')
        words = list(f)
        random.shuffle(words)
        print(("\n\n")+str(user)+str(", tes mots sont :\n\n")+str(words[0])+str(words[1])+str(words[2])+str(words[3]))

dictio()


