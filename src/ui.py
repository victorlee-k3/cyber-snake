"""
UI rendering engine for the Snake Game.
"""

import pygame
import random
import os
from typing import Tuple

from .config import (
    DIS_WIDTH, DIS_HEIGHT, BLOCK_SIZE,
    BG_COLOR, SNAKE_COLOR, FOOD_COLOR, 
    WHITE, TEXT_COLOR, TEXT_SHADOW, FONT_FILE
)
from .models import Snake, Food

class Renderer:
    def __init__(self, display: pygame.Surface) -> None:
        self.display = display
        # Render onto a subsurface to easily apply screen shake offsets
        self.render_surf = pygame.Surface((DIS_WIDTH, DIS_HEIGHT))
        self.shake_frames: int = 0
        self.shake_intensity: int = 5
        
        if os.path.exists(FONT_FILE):
            self.font_large = pygame.font.Font(FONT_FILE, 40)
            self.font_medium = pygame.font.Font(FONT_FILE, 20)
            self.font_small = pygame.font.Font(FONT_FILE, 14)
        else:
            self.font_large = pygame.font.Font(pygame.font.get_default_font(), 50)
            self.font_medium = pygame.font.Font(pygame.font.get_default_font(), 30)
            self.font_small = pygame.font.Font(pygame.font.get_default_font(), 20)

    def trigger_shake(self, frames: int = 10, intensity: int = 5) -> None:
        """Start the screen shake effect."""
        self.shake_frames = frames
        self.shake_intensity = intensity

    def clear(self) -> None:
        """Clear the rendering surface."""
        self.render_surf.fill(BG_COLOR)

    def draw_snake(self, snake: Snake) -> None:
        """Draw the snake with clean geometric shapes."""
        for i, (x, y) in enumerate(snake.body):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            if i == len(snake.body) - 1:
                # Head is slightly rounded differently
                pygame.draw.rect(self.render_surf, SNAKE_COLOR, rect, border_radius=6)
            else:
                # Body segments
                pygame.draw.rect(self.render_surf, SNAKE_COLOR, rect, border_radius=4)

    def draw_food(self, food: Food) -> None:
        """Draw the food as a geometric circle/rounded rect."""
        rect = pygame.Rect(food.position[0], food.position[1], BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(self.render_surf, FOOD_COLOR, rect, border_radius=BLOCK_SIZE // 2)

    def draw_score(self, score: int, high_score: int) -> None:
        """Render the current and high scores."""
        score_text = self.font_small.render(f"SCORE: {score}", True, TEXT_COLOR)
        score_shadow = self.font_small.render(f"SCORE: {score}", True, TEXT_SHADOW)
        
        hs_text = self.font_small.render(f"HIGH: {high_score}", True, TEXT_COLOR)
        hs_shadow = self.font_small.render(f"HIGH: {high_score}", True, TEXT_SHADOW)
        
        self.render_surf.blit(score_shadow, (12, 12))
        self.render_surf.blit(score_text, (10, 10))
        
        self.render_surf.blit(hs_shadow, (DIS_WIDTH - hs_shadow.get_width() - 8, 12))
        self.render_surf.blit(hs_text, (DIS_WIDTH - hs_text.get_width() - 10, 10))

    def _draw_overlay_text(self, title: str, subtitle: str) -> None:
        """Helper to draw semi-transparent overlays with text."""
        overlay = pygame.Surface((DIS_WIDTH, DIS_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180)) # Semi-transparent black
        self.render_surf.blit(overlay, (0, 0))
        
        title_surf = self.font_large.render(title, True, TEXT_COLOR)
        title_shadow = self.font_large.render(title, True, TEXT_SHADOW)
        
        sub_surf = self.font_medium.render(subtitle, True, WHITE)
        
        t_rect = title_surf.get_rect(center=(DIS_WIDTH // 2, DIS_HEIGHT // 2 - 40))
        ts_rect = title_shadow.get_rect(center=(DIS_WIDTH // 2 + 4, DIS_HEIGHT // 2 - 36))
        s_rect = sub_surf.get_rect(center=(DIS_WIDTH // 2, DIS_HEIGHT // 2 + 30))
        
        self.render_surf.blit(title_shadow, ts_rect)
        self.render_surf.blit(title_surf, t_rect)
        self.render_surf.blit(sub_surf, s_rect)

    def draw_start_menu(self) -> None:
        self._draw_overlay_text("CYBER SNAKE", "Press SPACE to Start")

    def draw_pause_menu(self) -> None:
        self._draw_overlay_text("PAUSED", "Press SPACE to Resume")

    def draw_game_over(self) -> None:
        self._draw_overlay_text("SYSTEM FAILURE", "Press C to Restart | Q to Quit")

    def render(self) -> None:
        """Blit the internal surface to the actual display, applying screen shake if active."""
        offset_x, offset_y = 0, 0
        if self.shake_frames > 0:
            offset_x = random.randint(-self.shake_intensity, self.shake_intensity)
            offset_y = random.randint(-self.shake_intensity, self.shake_intensity)
            self.shake_frames -= 1
            
        self.display.fill(BG_COLOR)  # clear background in case offset exposes edges
        self.display.blit(self.render_surf, (offset_x, offset_y))
        pygame.display.update()
