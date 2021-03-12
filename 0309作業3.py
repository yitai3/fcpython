# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:35:23 2021

@author: yiyiy
"""


import random

ans=random.randint(1,100)
guess=0

while ans != guess:  
    guess=int(input("請輸入1-00之間的整數:"))
    if guess > ans:
        minn=1
        guess == minn
        print("介於",minn,"~",guess,"之間")
    if guess < ans:
        maxx=100
        guess == maxx
        print("介於",guess,"~",maxx,"之間")
print("猜對了")      