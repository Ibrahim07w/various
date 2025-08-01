# 🧩 Random Crossword Puzzle Generator

This Python script generates **randomized word search puzzles** (crosswords) by embedding user-provided words in a grid. Words can appear horizontally, vertically, diagonally, or upward (bottom to top), and the remaining cells are filled with random letters.

---

## 🎯 Features

- ✅ Supports custom word lists
- ✅ Random placement in:
  - Horizontal
  - Vertical
  - Diagonal
  - Upward (bottom to top)
- ✅ Automatically avoids overlap conflicts
- ✅ Fills unused spaces with random letters
- ✅ Allows generation of multiple puzzles at once

---

## 🛠️ How It Works

- The grid is initialized with random letters.
- Each word is attempted to be placed randomly in one of the allowed directions.
- A helper function ensures the word fits and does not overwrite other placed words incorrectly.
- Once a word is successfully placed, its positions are marked as occupied.
- After all words are embedded, the final grid is printed.
