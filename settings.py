import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#CJ = os.path.join(AUDIO_DIR, "cj.wav")

# Color enumerators.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)
COLOR = RED
COUNTER = 0

BOTTOM_WALL = 690
LEFT_WALL = 0
RIGHT_WALL = 690
#DEBUG AND BOTS!
DEBUG = False
BOTS = True
AUDIO = False

PLAYER_SPRITE = {
    "file": "player.png",
    "size": [10, 10],
}
