import random
import pygame
from SetClass import cardSet
from collections import deque
from SetFinder import findAllSets

def generateDeck(): #genereert een gesoorteerde set deck
    index = [0,1,2]
    return [cardSet(n,c,s,sh) for n in index for c in index for s in index for sh in index]

def generateTable(): #pakt het de bovenste 12 kaarten van een geschudde set deck en kijkt of er een set in zit. Zo niet, wisseld het 3 nieuwe kaarten tot er wel een set is
    global deck
    global table
    deck = generateDeck()
    random.shuffle(deck)

    table = []
    for i in range(0,12):
        table.append(deck.pop())
    
    while len(findAllSets(table)) == 0 and deck: # the 'and deck' part ensures there are cards in the deck
        noSets(table)
    
    return table

def refillTable(table, deck):
    table = [card for card in table if not card.selected]

    while len(table) < 12 and deck: 
        table.append(deck.pop())
    
    while len(findAllSets(table)) == 0 and deck:
        noSets(table)
    return table


def noSets(cards): # wisseld 3 kaarten in voor 3 nieuwe kaarten
    cards = deque()

    for i in range(0,3):
        cards.append(deck.pop())
        cards.popleft()
