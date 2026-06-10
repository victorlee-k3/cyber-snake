"""
Data models for the Snake game entities.
"""

import random
from typing import List, Tuple
from .config import DIS_WIDTH, DIS_HEIGHT, BLOCK_SIZE

class Snake:
    def __init__(self) -> None:
        # Start at the center of the screen, perfectly aligned to grid
        start_x = int(round((DIS_WIDTH / 2) / float(BLOCK_SIZE)) * BLOCK_SIZE)
        start_y = int(round((DIS_HEIGHT / 2) / float(BLOCK_SIZE)) * BLOCK_SIZE)
        
        self.body: List[Tuple[int, int]] = [(start_x, start_y)]
        self.direction: str = ""
        self.next_direction: str = ""
        self.length: int = 1

    def handle_input(self, new_dir: str) -> None:
        """Buffer the next direction to prevent reverse-deaths."""
        if new_dir == "LEFT" and self.direction != "RIGHT":
            self.next_direction = "LEFT"
        elif new_dir == "RIGHT" and self.direction != "LEFT":
            self.next_direction = "RIGHT"
        elif new_dir == "UP" and self.direction != "DOWN":
            self.next_direction = "UP"
        elif new_dir == "DOWN" and self.direction != "UP":
            self.next_direction = "DOWN"

    def move(self) -> None:
        """Move the snake one block in the current direction."""
        if not self.next_direction:
            return  # Game hasn't started moving yet
            
        self.direction = self.next_direction
        
        head_x, head_y = self.body[-1]
        
        if self.direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            head_x += BLOCK_SIZE
        elif self.direction == "UP":
            head_y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            head_y += BLOCK_SIZE

        # Screen wrap-around logic
        if head_x >= DIS_WIDTH:
            head_x = 0
        elif head_x < 0:
            head_x = DIS_WIDTH - BLOCK_SIZE
            
        if head_y >= DIS_HEIGHT:
            head_y = 0
        elif head_y < 0:
            head_y = DIS_HEIGHT - BLOCK_SIZE

        new_head = (int(head_x), int(head_y))
        self.body.append(new_head)
        
        # Keep body length consistent unless grown
        if len(self.body) > self.length:
            del self.body[0]

    def grow(self) -> None:
        """Increase the snake's length by one."""
        self.length += 1

    def check_self_collision(self) -> bool:
        """Return True if the snake's head has collided with its body."""
        if len(self.body) < 2:
            return False
            
        head = self.body[-1]
        # Check all segments except the head itself
        if head in self.body[:-1]:
            return True
        return False

    def head_rect(self) -> Tuple[int, int, int, int]:
        """Return the bounding box for the head (x, y, w, h)."""
        return (self.body[-1][0], self.body[-1][1], BLOCK_SIZE, BLOCK_SIZE)


class Food:
    def __init__(self) -> None:
        self.position: Tuple[int, int] = (0, 0)
        self.randomize_position()

    def randomize_position(self) -> None:
        """Place food at a random grid-aligned position."""
        foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / float(BLOCK_SIZE)) * BLOCK_SIZE
        foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / float(BLOCK_SIZE)) * BLOCK_SIZE
        self.position = (int(foodx), int(foody))

    def rect(self) -> Tuple[int, int, int, int]:
        """Return the bounding box for the food (x, y, w, h)."""
        return (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE)
