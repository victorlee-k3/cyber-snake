import pygame

# Make sure Pygame is fully initialized before importing other modules
# that might rely on its font or display submodules.
pygame.init()

from src.engine import GameEngine

def main():
    engine = GameEngine()
    engine.run()

if __name__ == "__main__":
    main()
