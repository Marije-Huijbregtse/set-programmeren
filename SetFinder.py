def isSet(card1, card2, card3):
    """
    Determines whether three given cards form a valid set.

    A valid set is defined by the rule that for each attribute 
    (number, color, shape, and shade), the sum of the attribute values 
    across the three cards must be divisible by 3. This ensures that 
    the attributes are either all the same or all different.

    Args:
        card1: The first card object with attributes number, color, shape, and shade.
        card2: The second card object with attributes number, color, shape, and shade.
        card3: The third card object with attributes number, color, shape, and shade.

    Returns:
        bool: True if the three cards form a valid set, False otherwise.
    """
    return ( (card1.number + card2.number + card3.number)%3 == 0 
            and (card1.color + card2.color + card3.color)%3 == 0 
            and (card1.shape + card2.shape + card3.shape)%3 == 0 
            and (card1.shade + card2.shade + card3.shade)%3 == 0    
        )

def findOneSet(table):
    """
    Finds a single valid set from a list of cards.

    Iterates through all possible combinations of three cards in the 
    provided list and checks if any combination forms a valid set using 
    the `isSet` function.

    Args:
        cards: A list of card objects, where each card has attributes 
               such as number, color, shape, and shade.

    Returns:
        tuple or None: A tuple containing three cards that form a valid 
        set, or None if no set is found.
    """
    for combo in combinations(table, 3):
        if isSet(*combo):
            return combo
    return None

def findAllSets(cards):
    """
    Finds all valid sets in a given list of cards.

    Iterates through all possible combinations of three cards in the 
    provided list and checks each combination for validity using the 
    `isSet` function. Collects and returns all valid sets found.

    Args:
        cards: A list of card objects, where each card has attributes 
               such as number, color, shape, and shade.

    Returns:
        list: A list of tuples, where each tuple contains three cards 
        that form a valid set. Returns an empty list if no sets are found.
    """
    sets = []
    for combo in combinations(cards, 3):
        if isSet(*combo):
            sets.append(combo)
    return sets

def checkSelectedSet(cards):
    """
    Checks if the selected cards in a given list form a valid set.

    Filters the provided list of cards to identify those marked as 
    selected. If exactly three cards are selected, it determines 
    whether they form a valid set using the `isSet` function.

    Args:
        cards: A list of card objects, where each card has attributes 
               such as number, color, shape, shade, and a `selected` 
               attribute indicating whether the card is selected.

    Returns:
        bool: True if exactly three selected cards form a valid set, 
        False otherwise.
    """
    selected_cards = [card for card in cards if card.selected]
    if len(selected_cards) == 3:    
        if isSet(*selected_cards):
            return True
    return False

def combinations(iterable, r):
    """
    Makes all possible combinations of `r` elements from the given `iterable`.

    This function works like `itertools.combinations`, producing combinations 
    as tuples in lexicographic order. The input iterable is treated as a pool of elements, 
    and combinations are yielded without repetition.

    Args:
        iterable: An iterable from which we can draw elements (e.g., list, tuple, string).
        r (int): The number of elements in each combination.

    Returns:
        list: A list of tuples, where each tuple is a combination of `r` elements from 
        the input iterable. Returns an empty list if `r > len(iterable)`.
    """
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return []
    
    indices = list(range(r))
    result = [tuple(pool[i] for i in indices)]
    
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            break
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        result.append(tuple(pool[i] for i in indices))
    
    return result