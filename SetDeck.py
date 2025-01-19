import random
import pygame
from SetClass import cardSet
from collections import deque
from SetFinder import findAllSets


def generateDeck():
    """
    Generates a sorted Set deck.

    Creates a complete deck of Set cards by iterating through all 
    possible combinations of four attributes (number, color, shape, 
    and shade), each ranging from 0 to 2.

    Returns:
        list: A list of cardSet objects representing a complete, 
        sorted Set deck.
    """
    index = [0,1,2]
    return [cardSet(n,c,s,sh) for n in index for c in index for s in index for sh in index]


def generateTable():
    """
    Generates a table of 12 cards from a shuffled Set deck, ensuring at least one valid set is present.

    The function creates and shuffles a complete Set deck, then draws the top 12 cards to form the table.
    If no valid sets are found in the initial 12 cards, three cards are replaced at a time until 
    a valid set is present or the deck is exhausted.

    Uses:
        - `generateDeck()` to create a full deck.
        - `findAllSets()` to check for valid sets in the table.
        - `noSets()` to replace cards when no sets are found.

    Globals:
        deck (list): The shuffled deck of Set cards.
        table (list): The current table of cards drawn from the deck.

    Returns:
        list: A list of 12 cards ensuring at least one valid set exists.
    """
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
    """
    Refills the table to ensure it contains at least 12 cards, guaranteeing at least one valid set.

    Removes cards marked as selected from the current table, then adds cards from the deck until 
    the table contains at least 12 cards or the deck is exhausted. If no valid sets are found 
    on the table, replaces cards using `noSets()` until a valid set is present.

    Args:
        table (list): The current list of cards on the table, some of which may be marked as selected.
        deck (list): The remaining deck of Set cards.

    Returns:
        list: A table containing at least 12 cards with at least one valid set, if possible.
    """

    table = [card for card in table if not card.selected]

    while len(table) < 12 and deck: 
        table.append(deck.pop())
    
    while len(findAllSets(table)) == 0 and deck:
        noSets(table)
    return table


def noSets(table):
    """
    Replaces three cards on the left of the table with three new cards from the deck.

    This function is used when no valid sets are found on the table. It removes the 
    three leftmost cards from the table and replaces them with three new cards drawn 
    from the deck.

    Args:
        table (deque): A deque containing the current table of cards. The leftmost 
                       three cards are removed, and three new cards are added to the right.

    Returns:
        None
    """
    table = deque()

    for i in range(0,3):
        table.append(deck.pop())
        table.popleft()


def loadCardImages():
    """
    Loads card images from the 'kaarten' folder and returns a dictionary mapping card names to images.

    This function generates card names based on combinations of attributes (color, shape, shade, and number), 
    constructs file paths for the corresponding images, and loads the images using Pygame.

    Naming Pattern:
        - Colors: "green", "red", "purple"
        - Shapes: "diamond", "oval", "squiggle"
        - Shades: "empty", "filled", "shaded"
        - Numbers: "1", "2", "3"

    Each combination of these attributes forms a card name, and the corresponding image is loaded from 
    the 'kaarten' folder as a `.gif` file.

    Returns:
        dict: A dictionary where keys are card names (e.g., "greendiamondempty1") and values are 
        the loaded Pygame image objects.
    """
    cardImages = {}

    # Decode filenames based on naming pattern
    colors = ["green", "red", "purple"]
    shapes = ["diamond", "oval", "squiggle"]
    shades = ["empty", "filled", "shaded"]
    numbers = ["1", "2", "3"]

    for color in colors:
        for shape in shapes:
            for shade in shades:
                for number in numbers:
                    cardName = f"{color}{shape}{shade}{number}"            # FIgure out the card name based on atributes
                    imagePath = f"{"kaarten"}/{cardName}.gif"              # Create the file path to find the cards
                    cardImages[cardName] = pygame.image.load(imagePath)    # Load the image into pygame memory making it ready for using in the game

    return cardImages
