import pygame

# Function to handle first display and hover effect for cards
def drawTable(display, cards, mouse_pos, card_images):
    # Constants
    xStart = 50
    yStart = 20
    xSpacing = 120
    ySpacing = 200
    shadow_offset = 8  # Offset for the shadow
    shadow_color = (30, 30, 30)  # Shadow color
    shadow__select_color = (0, 152, 15) #Shadow select color
    card_grow_size = 115

    for i, card in enumerate(cards):
        cardName = f"{['green', 'red', 'purple'][card.color]}" \
                   f"{['diamond', 'oval', 'squiggle'][card.shape]}" \
                   f"{['empty', 'filled', 'shaded'][card.shade]}" \
                   f"{card.number + 1}"

        # Calculate card position
        x = xStart + (i % 4) * xSpacing
        y = yStart + (i // 4) * ySpacing

        # Create a rect for the card's hitbox
        card_rect = pygame.Rect(x, y, 100, 150)

        # Check if the card is selected or hovered
        if card.selected:
            # Enlarge the card and draw its shadow
            enlarged_shadow_rect = pygame.Rect(x + shadow_offset - 5, y + shadow_offset - 7, card_grow_size, card_grow_size * 1.5)
            pygame.draw.rect(display, shadow__select_color, enlarged_shadow_rect, border_radius=10)

            enlarged_image = pygame.transform.scale(card_images[cardName], (card_grow_size, card_grow_size * 1.5))
            display.blit(enlarged_image, (x - 5, y - 7))
        elif card_rect.collidepoint(mouse_pos):
            # Enlarge the card and draw its shadow
            enlarged_shadow_rect = pygame.Rect(x + shadow_offset - 5, y + shadow_offset - 7, card_grow_size, card_grow_size * 1.5)
            pygame.draw.rect(display, shadow_color, enlarged_shadow_rect, border_radius=10)

            enlarged_image = pygame.transform.scale(card_images[cardName], (card_grow_size, card_grow_size * 1.5))
            display.blit(enlarged_image, (x - 5, y - 7))
        else:
            # Draw the normal shadow
            shadow_rect = pygame.Rect(x + shadow_offset, y + shadow_offset, 100, 150)
            pygame.draw.rect(display, shadow_color, shadow_rect, border_radius=10)

            # Draw the card normally
            card_image = pygame.transform.scale(card_images[cardName], (100, 150))
            display.blit(card_image, (x, y))


def cardSelection(cards, mouse_pos):
    # Constants for card positioning
    xStart = 50
    yStart = 20
    xSpacing = 120
    ySpacing = 200

    # Count how many cards are currently selected
    selected_count = sum(1 for card in cards if card.selected)

    for i, card in enumerate(cards):
        # Calculate card position
        x = xStart + (i % 4) * xSpacing
        y = yStart + (i // 4) * ySpacing

        # Create a rect for the card's hitbox
        card_rect = pygame.Rect(x, y, 100, 150)

        if card_rect.collidepoint(mouse_pos):  # Check if the mouse clicked on this card
            if not card.selected and selected_count < 3:
                card.selected = True  # Select the card if fewer than 3 cards are already selected
            elif card.selected:
                card.selected = False  # Deselect the card
            break