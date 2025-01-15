from itertools import combinations
from SetClass import cardSet

def isSet(card1,card2,card3): # functie om te checken of 3 kaarten een set zijn of niet
    return ( (card1.number + card2.number + card3.number)%3 == 0 
            and (card1.color + card2.color + card3.color)%3 == 0 
            and (card1.shape + card2.shape + card3.shape)%3 == 0 
            and (card1.shade + card2.shade + card3.shade)%3 == 0    
        )

def findOneSet(cards): # functie om 1 set te vinden
    for combo in combinations(cards, 3):
        if isSet(*combo):
            return combo
    return None

def findAllSets(cards): # vind alle sets in een lijst (cards)
    sets = []
    for combo in combinations(cards, 3):
        if isSet(*combo):
            sets.append(combo)
    return sets

def checkSelectedSet(cards):
    selected_cards = [card for card in cards if card.selected]
    if len(selected_cards) == 3:    # Ensures the code doesn't crash
        if isSet(*selected_cards):  # Use the isSet function from SetFinder.py
            return True
    return False