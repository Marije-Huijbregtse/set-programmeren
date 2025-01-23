import pygame
import math # Needed for the drawTimer function


# Global constants
cardWidth = 100
cardHeight = 150
screenWidth = 800
screenHeight = 600
shadow_color = (0, 30, 3)  # Dark green shadow color

def drawCard(display, card_image, x, y, shadow_color, is_enlarged=False):
    """
    Draws a single card on the screen with optional shadow and enlargement.

    This function handles the rendering of a card's image on the display at a given position. 
    It also draws a shadow for the card, and optionally enlarges the card for highlighting purposes.

    Args:
        display: The Pygame display surface where the card will be drawn.
        card_image: The image of the card to be drawn.
        x (int): The x-coordinate of the top-left corner of the card's position.
        y (int): The y-coordinate of the top-left corner of the card's position.
        shadow_color: The color of the card's shadow.
        is_enlarged (bool, optional): If True, the card is drawn larger than normal to indicate selection 
                                       or focus. Defaults to False.

    Constants:
        - shadow_offset: The offset distance for the shadow relative to the card.
        - card_width, card_height: Dimensions of the card. Adjusted if the card is enlarged.
        - enlarged_offset: Adjustment for position when the card is enlarged.

    Returns:
        None: The function directly modifies the display surface.
    """
    shadow_offset = 8
    card_width = cardWidth if not is_enlarged else 115
    card_height = cardHeight if not is_enlarged else int(115 * 1.5)
    enlarged_offset = -5 if is_enlarged else 0
    
    # Draw shadow
    shadow_rect = pygame.Rect(
        x + shadow_offset + enlarged_offset, 
        y + shadow_offset + enlarged_offset, 
        card_width, 
        card_height
    )
    pygame.draw.rect(display, shadow_color, shadow_rect, border_radius=10)
    
    # Draw card image
    card_image = pygame.transform.scale(card_image, (card_width, card_height))
    display.blit(card_image, (x + enlarged_offset, y + enlarged_offset))

def drawTable(display, cards, mouse_pos, card_images):
    """
    Renders the entire table of cards, including their visual states (e.g., selected, hovered).

    This function calculates the position of each card on the table and renders it using the `drawCard` function. 
    The card's appearance changes based on its state:
      - Enlarged with a green shadow if selected.
      - Enlarged with a default shadow color if hovered over by the mouse.
      - Standard size with a default shadow color otherwise.

    Args:
        display: The Pygame display surface where the table will be drawn.
        cards (list): A list of card objects, each with attributes like `color`, `shape`, `shade`, `number`, 
                      and `selected` to indicate its state.
        mouse_pos (tuple): The (x, y) coordinates of the current mouse position, used to determine hover states.
        card_images (dict): A dictionary mapping card names (e.g., "greendiamondempty1") to their Pygame image objects.

    Constants:
        - xStart, yStart: Starting coordinates for the table layout.
        - xSpacing, ySpacing: Horizontal and vertical spacing between cards.
        - default_shadow_color: Shadow color for unselected cards.
        - selected_shadow_color: Shadow color for selected cards.

    Returns:
        None: The function directly modifies the display surface.
    """
    xStart, yStart = 50, 20
    xSpacing, ySpacing = 120, 200
    default_shadow_color = shadow_color
    selected_shadow_color = (0, 152, 15)
    
    for i, card in enumerate(cards):
        card_name = f"{['green', 'red', 'purple'][card.color]}" \
                    f"{['diamond', 'oval', 'squiggle'][card.shape]}" \
                    f"{['empty', 'filled', 'shaded'][card.shade]}" \
                    f"{card.number + 1}"
        
        # Calculate card position
        x = xStart + (i % 4) * xSpacing
        y = yStart + (i // 4) * ySpacing
        card_rect = pygame.Rect(x, y, cardWidth, cardHeight)
        
        # Determine state
        if card.selected:
            drawCard(display, card_images[card_name], x, y, selected_shadow_color, is_enlarged=True)
        elif card_rect.collidepoint(mouse_pos):
            drawCard(display, card_images[card_name], x, y, default_shadow_color, is_enlarged=True)
        else:
            drawCard(display, card_images[card_name], x, y, default_shadow_color)


def drawButton(display, text, x, y, width, height, inactive_color, text_color, is_active=False):
    """
    Draws a button with a 3D effect, including shadow details and centered text.

    The button's appearance changes based on its active state:
      - If `is_active` is True, the button appears indented with darker and lighter edges flipped.
      - Otherwise, the button has a raised effect with lighter top and left edges and darker bottom and right edges.

    Args:
        display: The Pygame display surface where the button will be drawn.
        text (str): The text to display on the button.
        x (int): The x-coordinate of the top-left corner of the button.
        y (int): The y-coordinate of the top-left corner of the button.
        width (int): The width of the button.
        height (int): The height of the button.
        inactive_color (tuple): The base color of the button in RGB format.
        text_color (tuple): The color of the button text in RGB format.
        is_active (bool, optional): If True, renders the button as indented. Defaults to False.

    Helper Function:
        - clamp(value): Ensures a value stays within the range of 0 to 255, used to adjust color brightness.

    Returns:
        None: The function directly modifies the display surface.
    """
    def clamp(value):
        return max(0, min(255, value))

    if is_active:
        # Indented effect: Flip the shadows
        pygame.draw.rect(display, inactive_color, (x, y, width, height))
        pygame.draw.line(display, (clamp(inactive_color[0] - 30), clamp(inactive_color[1] - 30), clamp(inactive_color[2] - 30)),
                         (x, y), (x + width, y), 3)  # Top edge (darker)
        pygame.draw.line(display, (clamp(inactive_color[0] - 30), clamp(inactive_color[1] - 30), clamp(inactive_color[2] - 30)),
                         (x, y), (x, y + height), 3)  # Left edge (darker)
        pygame.draw.line(display, (clamp(inactive_color[0] + 30), clamp(inactive_color[1] + 30), clamp(inactive_color[2] + 30)),
                         (x, y + height), (x + width, y + height), 3)  # Bottom edge (lighter)
        pygame.draw.line(display, (clamp(inactive_color[0] + 30), clamp(inactive_color[1] + 30), clamp(inactive_color[2] + 30)),
                         (x + width, y), (x + width, y + height), 3)  # Right edge (lighter)
    else:
        # Normal button
        pygame.draw.rect(display, inactive_color, (x, y, width, height))
        pygame.draw.line(display, (clamp(inactive_color[0] + 30), clamp(inactive_color[1] + 30), clamp(inactive_color[2] + 30)),
                         (x, y), (x + width, y), 3)  # Top edge
        pygame.draw.line(display, (clamp(inactive_color[0] + 30), clamp(inactive_color[1] + 30), clamp(inactive_color[2] + 30)),
                         (x, y), (x, y + height), 3)  # Left edge
        pygame.draw.line(display, (clamp(inactive_color[0] - 30), clamp(inactive_color[1] - 30), clamp(inactive_color[2] - 30)),
                         (x, y + height), (x + width, y + height), 3)  # Bottom edge
        pygame.draw.line(display, (clamp(inactive_color[0] - 30), clamp(inactive_color[1] - 30), clamp(inactive_color[2] - 30)),
                         (x + width, y), (x + width, y + height), 3)  # Right edge

    # Draw button text
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    display.blit(text_surface, text_rect)


def drawScores(display, player_score, computer_score, set_counter, deck_counter, x_offset, y_offset, text_color):
    """
    Draws the scores, set counter, and remaining cards on the screen.

    This function renders the player's score, computer's score, the number of possible sets, 
    and the remaining cards in the deck at specified positions on the display. Each piece of 
    information is drawn on a separate line with a vertical offset.

    Args:
        display: The Pygame display surface where the scores will be drawn.
        player_score (int): The player's current score.
        computer_score (int): The computer's current score.
        set_counter (int): The number of possible sets currently available on the table.
        deck_counter (int): The number of cards remaining in the deck.
        x_offset (int): The horizontal offset from the right edge of the screen.
        y_offset (int): The vertical offset from the top edge of the screen.
        text_color (tuple): The RGB color of the text.

    Constants:
        - screenWidth: The width of the screen, used to calculate text positioning.

    Returns:
        None: The function directly modifies the display surface.
    """
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


def drawTimer(display, x, y, radius, elapsed_ratio, base_color, time_color):
    """
    Draws a circular timer on the screen to visualize elapsed time.

    The timer consists of:
      - A shadow for a 3D effect.
      - A background circle representing the full time.
      - A colored arc showing the remaining time, where the length of the arc 
        is proportional to the `elapsed_ratio`.

    Args:
        display: The Pygame display surface where the timer will be drawn.
        x (int): The x-coordinate of the center of the timer.
        y (int): The y-coordinate of the center of the timer.
        radius (int): The radius of the timer circle.
        elapsed_ratio (float): The proportion of time elapsed, between 0 (no time passed) 
                               and 1 (all time passed).
        base_color (tuple): The RGB color of the background circle.
        time_color (tuple): The RGB color of the arc representing remaining time.

    Constants:
        - shadow_offset: The offset distance for the shadow to give a 3D effect.

    Returns:
        None: The function directly modifies the display surface.
    """
    shadow_offset = 4  # Offset for the shadow

    # Draw the shadow
    pygame.draw.circle(display, shadow_color, (x + shadow_offset, y + shadow_offset), radius)

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