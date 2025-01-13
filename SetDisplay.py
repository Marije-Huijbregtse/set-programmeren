import pygame
from DeckFunctions import generateTable
from SetInteractive import draw_button

# Initialize Pygame
pygame.init()

# Constants
screenWidth = 800
screenHeight = 600
cardWidth = 100
cardHeight = 150
background = (50, 50, 50)

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
# Function to draw cards on the table
def drawTable(cards):
    # Constants
    xStart = 50
    yStart = 20
    xSpacing = 120
    ySpacing = 200
    shadow_offset = 8  # Offset for the shadow
    shadow_color = (30, 30, 30)  # A darker shade for the shadow

    for i, card in enumerate(cards):
        cardName = f"{['green', 'red', 'purple'][card.color]}" \
                    f"{['diamond', 'oval', 'squiggle'][card.shape]}" \
                    f"{['empty', 'filled', 'shaded'][card.shade]}" \
                    f"{card.number + 1}"

        # Calculate card position
        x = xStart + (i % 4) * xSpacing
        y = yStart + (i // 4) * ySpacing

        # Draw the shadow first
        shadow_rect = pygame.Rect(x + shadow_offset, y + shadow_offset, cardWidth, cardHeight)
        pygame.draw.rect(display, shadow_color, shadow_rect, border_radius=10)

        # Draw the card image on top of the shadow
        card_image = pygame.transform.scale(cardImages[cardName], (cardWidth, cardHeight))
        display.blit(card_image, (x, y))



# Generate the initial table of cards
table = generateTable()

# Main interactive loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Checks if the player has closed the window
            running = False

    # Clear the screen
    display.fill(background)

    # Draw the table
    drawTable(table)

    # Draw the button
    button_x = screenWidth - 150 - 20
    button_y = screenHeight - 50 - 20
    draw_button(display, "Check Set", button_x, button_y, 150, 50, (70, 70, 70), (255, 255, 255))

    # Update the display after all drawing is complete
    pygame.display.flip()

# Quit the game
pygame.quit()
