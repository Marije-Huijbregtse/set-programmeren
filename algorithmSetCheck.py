frist = cardSet(0, 2, 1, 2)
second = cardSet(1, 2, 0, 1)
third = cardSet(2, 2, 2, 0)

def isSet(card1,card2,card3): #functie om te checken of 3 kaarten een set zijn of niet
    if (card1.number + card2.number + card3.number)%3 == 0:
        if (card1.color + card2.color + card3.color)%3 == 0:
            if (card1.shape + card2.shape + card3.shape)%3 == 0:
                if (card1.shade + card2.shade + card3.shade)%3 == 0:
                    print('set!')

isSet(first, second, third)