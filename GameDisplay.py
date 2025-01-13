from setclass import cardSet
import random
from collections import deque
from SetFinder import findAllSets


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


def noSets(cards): #wisseld 3 kaarten in voor 3 nieuwe kaarten
    cards = deque()

    for i in range(0,3):
        cards.append(deck.pop())
        cards.popleft()

print(generateDeck())
