import pygame
import math # Needed for the drawTimer function


# Global constants
cardWidth = 100
cardHeight = 150
screenWidth = 800
screenHeight = 600


def drawButton(display, text, x, y, width, height, inactive_color, text_color, is_active=False):
    if is_active:
        # Indented effect: Flip the shadows
        pygame.draw.rect(display, inactive_color, (x, y, width, height))
        pygame.draw.line(display, (inactive_color[0] - 30, inactive_color[1] - 30, inactive_color[2] - 30),
                         (x, y), (x + width, y), 3)  # Top edge (darker)
        pygame.draw.line(display, (inactive_color[0] - 30, inactive_color[1] - 30, inactive_color[2] - 30),
                         (x, y), (x, y + height), 3)  # Left edge (darker)
        pygame.draw.line(display, (inactive_color[0] + 30, inactive_color[1] + 30, inactive_color[2] + 30),
                         (x, y + height), (x + width, y + height), 3)  # Bottom edge (lighter)
        pygame.draw.line(display, (inactive_color[0] + 30, inactive_color[1] + 30, inactive_color[2] + 30),
                         (x + width, y), (x + width, y + height), 3)  # Right edge (lighter)
    else:
        # Normal button
        pygame.draw.rect(display, inactive_color, (x, y, width, height))
        pygame.draw.line(display, (inactive_color[0] + 30, inactive_color[1] + 30, inactive_color[2] + 30),
                         (x, y), (x + width, y), 3)  # Top edge
        pygame.draw.line(display, (inactive_color[0] + 30, inactive_color[1] + 30, inactive_color[2] + 30),
                         (x, y), (x, y + height), 3)  # Left edge
        pygame.draw.line(display, (inactive_color[0] - 30, inactive_color[1] - 30, inactive_color[2] - 30),
                         (x, y + height), (x + width, y + height), 3)  # Bottom edge
        pygame.draw.line(display, (inactive_color[0] - 30, inactive_color[1] - 30, inactive_color[2] - 30),
                         (x + width, y), (x + width, y + height), 3)  # Right edge

    # Draw button text
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    display.blit(text_surface, text_rect)


def drawScores(display, player_score, computer_score, set_counter, deck_counter, x_offset, y_offset, text_color):
    font = pygame.font.Font(None, 36)

    # Render player score
    player_score_text = font.render(f"Player: {player_score}", True, text_color)
    player_score_rect = player_score_text.get_rect(topright=(screenWidth - x_offset, y_offset))
    display.blit(player_score_text, player_score_rect)

    # Render computer score
    computer_score_text = font.render(f"Computer: {computer_score}", True, text_color)
    computer_score_rect = computer_score_text.get_rect(topright=(screenWidth - x_offset, y_offset + 40))  # Offset for second line
    display.blit(computer_score_text, computer_score_rect)

    # Render set counter
    set_counter_text = font.render(f"Possible sets: {set_counter}", True, text_color)
    set_counter_rect = set_counter_text.get_rect(topright=(screenWidth - x_offset, y_offset + 80))  # Offset for third line
    display.blit(set_counter_text, set_counter_rect)

    # Render deck counter
    deck_counter_text = font.render(f"Cards left: {deck_counter}", True, text_color)
    deck_counter_rect = deck_counter_text.get_rect(topright=(screenWidth - x_offset, y_offset + 120))  # Offset for fourth line
    display.blit(deck_counter_text, deck_counter_rect)

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


def drawTimer(display, x, y, radius, elapsed_ratio, base_color, time_color):
    # Draw the background circle
    pygame.draw.circle(display, base_color, (x, y), radius)

    # Draw the remaining time as an arc
    remaining_angle = math.pi * 2 * (1 - elapsed_ratio)
    pygame.draw.arc(
        display,
        time_color,
        (x - radius, y - radius, 2 * radius, 2 * radius),
        -math.pi / 2,  # Start angle at the top
        -math.pi / 2 + remaining_angle,  # End angle based on elapsed time
        width=10
    )