import pygame
from DeckFunctions import generateTable

# Initialize Pygame
pygame.init()

# Constants
screenWidth = 800
screenHeight = 600
cardWidth = 100
cardHeight = 150
white = (50, 50, 50)

# Create the Pygame screen
display = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("SET Game Display")

# Load card images from the 'kaarten' folder
def loadCardImages():
    cardImages = {}

    # Hardcoded filenames based on known naming convention
    colors = ["green", "red", "purple"]
    shapes = ["diamond", "oval", "squiggle"]
    shades = ["empty", "filled", "shaded"]
    numbers = ["1", "2", "3"]

    for color in colors:
        for shape in shapes:
            for shade in shades:
                for number in numbers:
                    cardName = f"{color}{shape}{shade}{number}"            # Deduce the card name based on atributes
                    imagePath = f"{"kaarten"}/{cardName}.gif"              # Creathe image path to find the cards
                    cardImages[cardName] = pygame.image.load(imagePath)    # Load the image into pygame memory making it ready for rendering in the game

    return cardImages

# Creating a dictionary in which the card images are stored
cardImages = loadCardImages()

# Function to draw cards on the table
def drawTable(cards):
    display.fill(white)  # Clear the screen

    # Constants
    xStart = 50
    yStart = 20
    xSpacing = 120
    ySpacing = 200

    # Deduce the card name based on atributes
    for i, card in enumerate(cards):
        cardName = f"{['green', 'red', 'purple'][card.color]}" \
                    f"{['diamond', 'oval', 'squiggle'][card.shape]}" \
                    f"{['empty', 'filled', 'shaded'][card.shade]}" \
                    f"{card.number + 1}"

        # Calculate card position
        x = xStart + (i % 4) * xSpacing
        y = yStart + (i // 4) * ySpacing

        # Scale the card images to fit the specified dimensions and draw them on the screen
        display.blit(pygame.transform.scale(cardImages[cardName], (cardWidth, cardHeight)), (x, y)) 

    # Refresh the screen
    pygame.display.flip()

# Generate the initial table of cards
table = generateTable()

# Create boolean value defining whether the game runs or not
running = True

# determines whether to continue or quit the game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if the player has closed the window
            running = False

    drawTable(table)

# Will quit the game when the while loop ends
pygame.quit()