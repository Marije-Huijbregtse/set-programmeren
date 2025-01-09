from setclass import cardSet
import random
from itertools import combinations
from collections import deque

def isSet(card1,card2,card3): #functie om te checken of 3 kaarten een set zijn of niet
    return ( (card1.number + card2.number + card3.number)%3 == 0 
            and (card1.color + card2.color + card3.color)%3 == 0 
            and (card1.shape + card2.shape + card3.shape)%3 == 0 
            and (card1.shade + card2.shade + card3.shade)%3 == 0    
        )


def findOneSet(cards): #functie om 1 set te vinden
    for combo in combinations(cards, 3):
        if isSet(*combo):
            return combo
    return None

def generateDeck(): #genereert een ongesoorteerde set deck
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
    
    while len(findAllSets()) == 0:
        noSets()


def findAllSets(cards): #vind alle sets in een lijst (cards)
    sets = []
    for combo in combinations(cards, 3):
        if isSet(*combo):
            sets.append(combo)
    return sets

def noSets(cards): #wisseld 3 kaarten in voor 3 nieuwe kaarten
    cards = deque()

    for i in range(0,3):
        cards.append(deck.pop())
        cards.popleft()

print(5)