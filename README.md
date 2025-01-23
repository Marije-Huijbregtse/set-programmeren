Getting Started
Step 1: Install the Required Software
To run the SET game, you need Python and the Pygame library installed on your computer.

Install Python:
    Download and install Python from https://www.python.org/downloads/.
Ensure you add Python to your system PATH during installation.

Install Pygame:
Open a command prompt or terminal and run:
    ‘pip install pygame’

Step 2: Prepare the Game Files
Download all the game files and ensure they are in the same folder.
Make sure the ‘kaarten’ folder contains the images for the cards and the background image.

How to Play
Step 1: Start the Game
Open a command prompt or terminal.
Navigate to the folder containing the game files.
Run the game by typing:
    python SetDisplay.py
Or just executing the folder SetDisplay.py

The game window will open, displaying a table with 12 cards.

Step 2: Understand the Rules
A "SET" is a group of three cards where each attribute (number, color, shape, and shading) is either all the same or all different.
Your goal is to find as many valid SETs as possible.

Step 3: Interact with the Game
Select Cards:
Click on a card to select it.
Click again to deselect it.
You can select up to three cards.

Check for a SET:
After selecting three cards, click the "Check Set" button at the bottom of the screen.

If the selected cards form a valid SET:
They will be replaced with new cards.
Your score will increase.
If they don’t form a valid SET, you’ll see a message saying "Not a set."

Timer:
The game is timed, so find as many SETs as you can before time runs out. When you find a SET, the timer will be reset. When the 30 second timer runs out, the computer will find a set and get a point instead. 

End of Game:
When the deck is emptied and no more SETs can be made, the game is done.
The final screen will display the scores for you and the computer.
Pressing '0' will remove the remaining cards in the deck.
This is useful for quickly ending the game.


Customization Options
Change the Background Image
Replace the file PokerCloth.jpg in the ‘kaarten’ folder with your desired background image.
Ensure the new image has the same name (PokerCloth.jpg) and dimensions as the original.


Replace Card Images
Replace card images in the ‘kaarten’ folder with your custom designs.
Use the same file names and formats as the original images to avoid issues.


Adjust the Timer
Find the line that says:
total_time = 30000  # 30 seconds in milliseconds
Change 30000 to your desired duration in milliseconds (e.g., 60000 for 1 minute).


Troubleshooting
Game doesn’t start:
Ensure Python and Pygame are installed correctly.
Check that all game files are in the same folder.

Images don’t load:
Verify that the ‘kaarten’ folder contains the necessary card images and background image.

Errors appear in the terminal:
Read the error message and ensure you didn’t accidentally delete or rename critical files.


Running the Game
To summarize, here’s how to play:
Install Python and Pygame.
Place all files in the same folder.
Run the game with:
    python SetDisplay.py
Enjoy finding SETs!