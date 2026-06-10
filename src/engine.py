"""
Game Engine handling logic, states, and game loop.
"""

import pygame
import sys
import json
import os

from .config import FPS, MOVE_INTERVAL_MS, HIGHSCORE_FILE, DIS_WIDTH, DIS_HEIGHT
from .models import Snake, Food
from .ui import Renderer

# Game States
STATE_START = 0
STATE_PLAYING = 1
STATE_PAUSED = 2
STATE_GAME_OVER = 3

class GameEngine:
    def __init__(self) -> None:
        self.display = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
        pygame.display.set_caption('Cyber Snake')
        self.clock = pygame.time.Clock()
        
        self.renderer = Renderer(self.display)
        self.snake = Snake()
        self.food = Food()
        
        self.state = STATE_START
        self.score = 0
        self.high_score = self.load_high_score()
        
        self.move_accumulator = 0

    def load_high_score(self) -> int:
        """Load the high score from the local JSON file."""
        if os.path.exists(HIGHSCORE_FILE):
            try:
                with open(HIGHSCORE_FILE, 'r') as f:
                    data = json.load(f)
                    return data.get("high_score", 0)
            except (json.JSONDecodeError, IOError):
                return 0
        return 0

    def save_high_score(self) -> None:
        """Save the high score to the local JSON file."""
        try:
            with open(HIGHSCORE_FILE, 'w') as f:
                json.dump({"high_score": self.high_score}, f)
        except IOError:
            pass

    def reset_game(self) -> None:
        """Reset the game state for a new round."""
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.state = STATE_PLAYING
        self.move_accumulator = 0

    def handle_events(self) -> None:
        """Process all pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
                
            if event.type == pygame.KEYDOWN:
                if self.state == STATE_START:
                    if event.key == pygame.K_SPACE:
                        self.state = STATE_PLAYING
                
                elif self.state == STATE_PLAYING:
                    if event.key == pygame.K_SPACE:
                        self.state = STATE_PAUSED
                    else:
                        if event.key == pygame.K_LEFT:
                            self.snake.handle_input("LEFT")
                        elif event.key == pygame.K_RIGHT:
                            self.snake.handle_input("RIGHT")
                        elif event.key == pygame.K_UP:
                            self.snake.handle_input("UP")
                        elif event.key == pygame.K_DOWN:
                            self.snake.handle_input("DOWN")
                            
                elif self.state == STATE_PAUSED:
                    if event.key == pygame.K_SPACE:
                        self.state = STATE_PLAYING
                        
                elif self.state == STATE_GAME_OVER:
                    if event.key == pygame.K_c:
                        self.reset_game()
                    elif event.key == pygame.K_q:
                        self.quit_game()

    def update(self, dt: int) -> None:
        """Update game logic using accumulated delta time."""
        if self.state != STATE_PLAYING:
            return
            
        self.move_accumulator += dt
        
        # Only move when accumulator exceeds the set interval
        if self.move_accumulator >= MOVE_INTERVAL_MS:
            self.move_accumulator -= MOVE_INTERVAL_MS
            self.snake.move()
            
            # Check collisions
            if self.snake.check_self_collision():
                self.handle_game_over()
                return
                
            # Check food collision
            head_rect = pygame.Rect(self.snake.head_rect())
            food_rect = pygame.Rect(self.food.rect())
            
            if head_rect.colliderect(food_rect):
                self.score += 1
                if self.score > self.high_score:
                    self.high_score = self.score
                self.snake.grow()
                self.food.randomize_position()
                self.renderer.trigger_shake(frames=6, intensity=6)

    def handle_game_over(self) -> None:
        """Handle game over state and save score."""
        self.state = STATE_GAME_OVER
        self.save_high_score()

    def render(self) -> None:
        """Command the renderer to draw the current state."""
        self.renderer.clear()
        
        if self.state in [STATE_PLAYING, STATE_PAUSED, STATE_GAME_OVER]:
            self.renderer.draw_food(self.food)
            self.renderer.draw_snake(self.snake)
            self.renderer.draw_score(self.score, self.high_score)
            
        if self.state == STATE_START:
            self.renderer.draw_start_menu()
        elif self.state == STATE_PAUSED:
            self.renderer.draw_pause_menu()
        elif self.state == STATE_GAME_OVER:
            self.renderer.draw_game_over()
            
        self.renderer.render()

    def run(self) -> None:
        """Main game loop."""
        while True:
            dt = self.clock.tick(FPS)
            self.handle_events()
            self.update(dt)
            self.render()

    def quit_game(self) -> None:
        self.save_high_score()
        pygame.quit()
        sys.exit()
