"""
Configuration constants for the Snake Game.
"""

from typing import Tuple

# Screen Settings
DIS_WIDTH: int = 800
DIS_HEIGHT: int = 600
BLOCK_SIZE: int = 20

# Framerate and Timing
FPS: int = 60
# Milliseconds between snake movements (lower is faster)
MOVE_INTERVAL_MS: int = 70 

# Cyberpunk UI Colors
BG_COLOR: Tuple[int, int, int] = (26, 26, 26)        # Deep slate-gray (#1a1a1a)
SNAKE_COLOR: Tuple[int, int, int] = (0, 255, 136)    # Neon-mint green (#00ff88)
FOOD_COLOR: Tuple[int, int, int] = (255, 85, 85)     # Crimson-coral (#ff5555)
WHITE: Tuple[int, int, int] = (255, 255, 255)
TEXT_COLOR: Tuple[int, int, int] = (0, 255, 136)
TEXT_SHADOW: Tuple[int, int, int] = (10, 50, 25)

# Game Files
HIGHSCORE_FILE: str = "highscore.json"
FONT_FILE: str = "retro_font.ttf"
