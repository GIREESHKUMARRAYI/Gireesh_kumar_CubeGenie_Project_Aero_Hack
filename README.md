# CubeGenie 🧊

**CubeGenie** is a modular and scalable Rubik’s Cube solver built using Python. It models the real-world cube behavior, applies valid face moves, and includes a live GUI visualizer using Tkinter.

---

## 📦 Features

- Full support for standard 3x3 Rubik’s Cube logic
- Accurate face rotation and move tracking
- Beginner-style solving logic (placeholder)
- Built-in GUI visualizer using Tkinter
- Modular code – easily extendable to NxN cubes or advanced algorithms

---

## ▶️ How to Run

1. Unzip the project folder
2. Open a terminal or command prompt in that folder
3. Run:

```bash
python main.py
```

---

## 🧰 Requirements

- Python 3.7+
- `tkinter` (built-in for Windows/macOS, install manually for Linux)

For Linux:
```bash
sudo apt-get install python3-tk
```

---

## 📂 File Structure

```
CubeGenie/
├── cube_state.py         # Defines the Cube object and internal state
├── move_engine.py        # All move logic (U, D, L, R, F, B and their inverses)
├── beginner_solver.py    # Basic placeholder solver logic
├── gui_visualizer.py     # GUI interface to display the cube
├── main.py               # Scrambles, solves, and launches GUI
└── README.md             # Instructions and info (this file)
```

---

## 🧪 Demo

- Scramble: `['R', 'U', "R'", 'U', 'R', 'U2', "R'"]`
- Solver Output: `['U', 'U', 'U', 'U']` (sample output for demo purposes)
- Live visualization displayed with face colors and orientation

---

## 🚀 Future Improvements

- Full beginner 7-step solving logic
- Add optimal solver (e.g., Kociemba’s algorithm)
- Support for 2x2, 4x4 cubes
- Web-based UI (React or Streamlit)

---

## 👥 Authors

Made By Gireesh Kumar Rayi for AeroHack’25
