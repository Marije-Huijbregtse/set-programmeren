import pygame
from SetDeck import generateTable

# Generate the initial table of cards and will run this fucntion to be able to import 'deck'
table = generateTable()

from SetDeck import refillTable, noCards, deck
from SetDraw import drawButton, drawScores, loadCardImages,drawTimer
from SetInteractive import drawTable, cardSelection
from SetFinder import checkSelectedSet, findOneSet, findAllSets

# Initialize Pygame
pygame.init()

# Constants
screenWidth = 800
screenHeight = 600
background = (50, 50, 50)

# Create the Pygame screen
display = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("SET Game Display")

# Initialize card images
cardImages = loadCardImages()

# Main interactive loop
running = True
endGame = False

# Initialize scores
player_score = 0
computer_score = 0

# Initialize button constants
button_pressed = False
button_x = screenWidth - 150 - 20
button_y = screenHeight - 50 - 20

# Initialize game over end screen time delay
delay = 0

# Timer settings
total_time = 30000  # 30 seconds in milliseconds
start_time = pygame.time.get_ticks()  # Record the start time
time_elapsed = 0

# Current message and its timestamp
current_message = None
message_start_time = 0  # Timestamp when the message was set
message_display_duration = 1000  # Duration to display the message (in milliseconds)

while running:
    current_time = pygame.time.get_ticks()
    time_elapsed = current_time - start_time
    elapsed_ratio = time_elapsed / total_time

    # Calculate the remaining time in seconds and milliseconds
    remaining_time = max(0, (total_time - time_elapsed) // 1000)
    remaining_milliseconds = (total_time - time_elapsed) % 1000

    # Blink the timer every half second during the last 5 seconds
    if 0 <= remaining_time <= 5:
        blink = (remaining_milliseconds // 500) % 2 == 1
    else:
        blink = True  # Timer is always visible outside the last 5 seconds

    # Check if the current message has expired
    if current_message and pygame.time.get_ticks() - message_start_time > message_display_duration:
        current_message = None  # Clear the current message

    # Display default countdown messages if no overriding message
    if not current_message:
        if remaining_time == 20:
            current_message = "20 seconds left!"
        elif remaining_time == 10:
            current_message = "10 seconds left!"
        elif 0 <= remaining_time <= 5:
            current_message = str(remaining_time)

    if time_elapsed >= total_time:
        current_message = "Computer has found a set!"
        message_start_time = pygame.time.get_ticks()
        computer_score += 1
        computer_Set = findOneSet(table)
        for card in table:
            if card in computer_Set:
                card.selected = True # Selects the cards in the computer found set
            else:
                card.selected = False # Ensures only the set the computer found will be selected

        # Clear the screen
        display.fill(background)
        drawTable(display, table, pygame.mouse.get_pos(), cardImages) # Only draws the table, no scores/timer/message/button

        pygame.display.flip()
        pygame.time.delay(3000)
        table = refillTable(table, deck)
        start_time = pygame.time.get_ticks()
        if len(table) < 12 or len(findAllSets(table)) == 0:
            endGame = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            cardSelection(table, mouse_pos)
            if button_x <= mouse_pos[0] <= button_x + 150 and button_y <= mouse_pos[1] <= button_y + 50:
                button_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if button_pressed and button_x <= mouse_pos[0] <= button_x + 150 and button_y <= button_y + 50:
                if checkSelectedSet(table):
                    player_score += 1
                    current_message = "Good job!"
                    message_start_time = pygame.time.get_ticks()
                    table = refillTable(table, deck)
                    start_time = pygame.time.get_ticks()
                    if len(table) < 12 or len(findAllSets(table)) == 0:
                        endGame = True
                else:
                    current_message = "Not a set"
                    message_start_time = pygame.time.get_ticks()
                button_pressed = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                deck = []

    # Clear the screen
    display.fill(background)

    if endGame:
        # Clear the screen
        display.fill(background)

        # Display the final scores
        font = pygame.font.Font(None, 60)
        player_score_text = font.render(f"Player Score: {player_score}", True, (255, 255, 255))
        computer_score_text = font.render(f"Computer Score: {computer_score}", True, (255, 255, 255))

        # Center the text on the screen
        player_rect = player_score_text.get_rect(center=(screenWidth // 2, screenHeight // 2 - 50))
        computer_rect = computer_score_text.get_rect(center=(screenWidth // 2, screenHeight // 2 + 50))

        # Draw the text
        display.blit(player_score_text, player_rect)
        display.blit(computer_score_text, computer_rect)

        # Update the display
        pygame.display.flip()

        # Wait for a moment before quitting
        pygame.time.delay(3000)
        running = False
        continue

    # Draw the timer (blink effect in last 5 seconds)
    if blink:
        drawTimer(display, 580, 40, 30, elapsed_ratio, (70, 70, 70), (255, 0, 0))
        

    # Display the current message
    if current_message:
        font_size = 60 if remaining_time <= 5 else 36
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(current_message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(650, 280))
        display.blit(text_surface, text_rect)


    # Draw the table
    drawTable(display, table, pygame.mouse.get_pos(), cardImages)

    # Draw the button
    drawButton(display, "Check Set", button_x, button_y, 150, 50, (70, 70, 70), (255, 255, 255), is_active=button_pressed)

    # Draw the scores
    drawScores(display, player_score, computer_score, len(findAllSets(table)), len(deck), 20, 20, (255, 255, 255))



    # Update the display
    pygame.display.flip()

pygame.quit()
