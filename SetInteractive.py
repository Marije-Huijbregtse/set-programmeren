import pygame

def draw_button(display, text, x, y, width, height, inactive_color, text_color):
    """
    Draws an indented button at the specified position.
    """
    # Outer rectangle (darker gray for the indented effect)
    pygame.draw.rect(display, inactive_color, (x, y, width, height))

    # Inner shadow effect (lighter edges for bevel)
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
