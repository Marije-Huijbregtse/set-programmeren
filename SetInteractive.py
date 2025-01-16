import pygame

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