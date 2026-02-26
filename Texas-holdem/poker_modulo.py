import json 
import os
import random
from datetime import datetime
from collections import Counter

FILE_RISULTATI = "risultati.json"

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K", "A"]
SEMI = ["F", "Q", "C", "P"]
SEMI_SIMBOLI = {
    "F": "\u2663",
    "Q": "\u2666",
    "C": "\u2665",
    "p": "\u2660"}

RANK_VALUE = {r: i for i, r in enumerate(RANKS,start=2)}


"""for i, r in enumerate(RANKS, start=2):
    print(i,r)"""

HANDS_VALUE = {
    9: "Scala reale",
    8: "Scala colore",
    7: "Poker",
    6: "Full",
    5: "Colore",
    4: "Scala",
    3: "Tris",
    2: "Doppia coppia",
    1: "Coppia",
    0: "Carta alta",
}

def createDeck():
    return [r + s for r in RANKS for s in SEMI]

"""quello che vediamo con il createDeck"""
"""deck = []
for r in RANKS:
    for s in SEMI:
        deck.append(r + s)
        
print(deck)"""

""" Associamo i somboli alle carte """
def prettyCards(cards):
    return " ".join([c[0] + SEMI_SIMBOLI.get(c[1], c[1]) for c in cards])

def isStraight(values):
    if len(values) < 5:
        return False, None
    
    wheel = {14, 5, 4, 3, 2,}
    if set(values) >= wheel:
        return True, 5
    
    vals = sorted(set(values), reverse=True)
    for i in range(len(vals) - 4):
        window = vals[i:i+5]
        if window[0] - window[4] == 4:
            return True, window[0]
    return False, None

""" Valuta una mano di 5 carte (funzione evaluate_5 1 di 4)"""

def evaluate_5(cards5):
    values = sorted([RANK_VALUE[c[0]] for c in cards5], reverse=True)
    semi = [c[1] for c in cards5]

    counts = Counter(values)
    countsGroups = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    flush = len(set(semi)) == 1
    uniqueValues = sorted(set(values), reverse=True)
    straight, straightHigh = isStraight(uniqueValues)

    if flush and straight:
        if straightHigh == 14:
            return(9,)
        return (8, straightHigh)
    
    if countsGroups[0][1] == 4:
        quad = countsGroups[0][0]
        kicker = max(v for v in values if v != quad)
        return (7, quad, kicker)
    
    if countsGroups[0][1] == 3 and countsGroups [1] [1] == 2:
        return(6, countsGroups[0][0], countsGroups[1][0])
    
    if flush:
        return (5, *values)
    
    if straight:
        return (4, straightHigh)
    
    if countsGroups[0][1] == 3:
        trips = countsGroups[0][0]
        kickers = sorted([v for v in values if v != trips], reverse=True)
        return (3, trips, *kickers)
    
    if countsGroups[0][1] == 2 and countsGroups[1][1] == 2:
        highPair = max(countsGroups[0][0], countsGroups [1][0])
        lowPair = min(countsGroups[0][0], countsGroups[1][0])
        kicker = max(v for v in values if v not in (highPair, lowPair))
        return (2, highPair, lowPair, kicker)
    
    if countsGroups[0][1] == 2:
        pair = countsGroups[0][0]
        kicker = sorted([v for v in values if v != pair], reverse=True)
        return (1, pair, *kicker)
    
    return (0, *values)