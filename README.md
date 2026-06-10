# 🐍 Cyber Snake 

A premium, production-ready, minimalist cyberpunk reimagining of the classic Snake game, built in Python using Pygame.

> _Insert a vibrant screenshot of the game here._
> `![Gameplay Screenshot](placeholder_gameplay.png)`

## 🌟 Features

- **Delta-Time Engine**: Buttery smooth 60 FPS rendering completely decoupled from grid-movement logic. Say goodbye to frame-lag and input-dropping.
- **Minimalist Cyberpunk UI**: Flat geometry, anti-aliased rounded rectangles, and a deep, high-contrast palette.
- **Juicy Game Feel**: Features dynamic screen-shake effects when eating apples to make gameplay feel impactful.
- **Infinite Screen Wrap**: Hitting walls is for amateurs. Go out the left screen, appear on the right! 
- **Persistent High Scores**: Automatically saves your best local scores between sessions.
- **State Machine UI**: Includes a Start Menu, Pause Overlay (press `SPACE`), and an elegant Game Over overlay.
- **Clean OOP Architecture**: Fully refactored codebase following rigorous Object-Oriented design, MVC-inspired separation of concerns, and PEP 8 guidelines.

## 📁 Repository Architecture

The project is structured into logical modules to ensure scalability and maintainability:

```text
cyber-snake/
├── main.py              # Application entry point
├── src/
│   ├── config.py        # Global settings, constants, and color palette
│   ├── engine.py        # Game loop, state machine, and delta-time controller
│   ├── models.py        # Snake and Food data structures (The 'Model')
│   └── ui.py            # Pygame rendering, overlays, and effects (The 'View')
├── highscore.json       # Generated local save file
├── retro_font.ttf       # Font asset (if downloaded)
└── README.md            # This file
```

## 🚀 Installation & Setup

1. **Prerequisites**
   Ensure you have Python 3.x installed.

2. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/cyber-snake.git
   cd cyber-snake
   ```

3. **Set up a Virtual Environment (Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**
   The only dependency is Pygame:
   ```bash
   pip install pygame
   ```

5. **Run the Game**
   ```bash
   python main.py
   ```

## 🎮 Controls

- **Arrow Keys** (`UP`, `DOWN`, `LEFT`, `RIGHT`): Change the snake's direction.
- **SPACE**: Start game, Pause game, Resume game.
- **C**: Restart after a Game Over.
- **Q**: Quit the application.

## 🛠 Contributing
Feel free to open issues or submit PRs if you want to add sound effects, new game modes, or particle systems!

---
_Built with Python and Pygame._
