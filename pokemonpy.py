# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 13:16:51 2019

@author: PC USER
"""
import csv
import pandas as pd
import json
from operator import itemgetter

pokedex = []
sortedList = []

def hello():
    print("Hello")
    
def printFile():   
    with open('Pokemon_all.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count < 100:
                print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} | {row[9]} | {row[10]} | {row[12]} | {row[13]}')
                line_count += 1      
        print(f'Processed {line_count} lines.')
    
def createPokedex():
    with open('Pokemon_all.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count <= 0:
                line_count += 1
            else:
                pokedex.append({'id':row[0], 'name':row[1], 'type1':row[2], 'type2':row[3], 'total':row[4], 'hp':row[5], 'attack':row[6], 'defense':row[7], 'spatk':row[8], 'spdef':row[9], 'speed':row[10], 'generation':row[11], 'legendary':row[12], 'mega':row[13]})
                line_count += 1
    return pokedex
    print(f'Processed {line_count} lines.')
    
def pokeSort():
    sortedList = pokedex
    sorter = input("Enter what you would like to sort by:")
    if sorter not in pokedex[0].keys():
        raise ValueError("BAD KEY NAME")
    else:
        sortedList = sorted(pokedex, key=lambda item: int(item[str(sorter)]))
        return sortedList
    
createPokedex()
for item in pokeSort():
    print(str(item) + '\n')


'''      
def attackSort():
    sortedList = pokedex
    sortedList = sorted(pokedex, key=lambda item: int(item['attack']))
    return sortedList
'''

'''
for item in attackSort():
    print(str(item) + '\n -------------------------------------------------------------------------------')
'''



    