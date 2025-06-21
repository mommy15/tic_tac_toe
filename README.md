<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">


# TIC_TAC_TOE

<em>Master Strategy, Outsmart Opponents, Play with Confidence</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/mommy15/tic_tac_toe?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/mommy15/tic_tac_toe?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/mommy15/tic_tac_toe?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Roadmap](#roadmap)

---

## Overview

tic_tac_toe is an open-source web application that combines a simple user interface with a powerful AI engine to deliver an engaging Tic-Tac-Toe experience. Built with a clear separation of concerns, it demonstrates how to integrate AI decision-making into interactive web apps efficiently.

**Why tic_tac_toe?**

This project provides a straightforward yet robust example of embedding AI logic into web applications. The core features include:

- 🧠 **[Emoji] AI Decision Engine:** Implements an optimal move selection using minimax with alpha-beta pruning, ensuring challenging gameplay.
- 🌐 **[Emoji] Web Server:** Handles user interactions, game rendering, and move processing, enabling real-time gameplay.
- 🎮 **[Emoji] Interactive Frontend:** Offers an intuitive interface for players to engage with the game and see updates instantly.
- 🔄 **[Emoji] Seamless Backend-Frontend Communication:** Facilitates smooth data exchange for a fluid user experience.
- 🛠️ **[Emoji] Modular Architecture:** Promotes maintainability and easy extension of game features.

---

## Features

|      | Component       | Details                                                                                     |
| :--- | :-------------- | :------------------------------------------------------------------------------------------ |
| ⚙️  | **Architecture**  | <ul><li>Single-page application with HTML frontend</li><li>Python backend for game logic</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Clear separation of concerns between UI and logic</li><li>Readable, concise Python code</li></ul> |
| 📄 | **Documentation** | <ul><li>Basic README with project overview</li><li>Inline comments in code for functions</li></ul> |
| 🔌 | **Integrations**  | <ul><li>HTML for UI rendering</li><li>Python scripts for game state management</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separate modules for game logic and UI</li><li>Functions for move validation, game status</li></ul> |
| 🧪 | **Testing**       | <ul><li>Limited or no automated tests observed</li><li>Potential for unit tests on game logic functions</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Lightweight, runs efficiently in browser</li><li>Minimal computational overhead</li></ul> |
| 🛡️ | **Security**      | <ul><li>Basic, no authentication or data security measures</li><li>Client-side game logic only</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Python standard library</li><li>HTML for frontend</li></ul> |

---

## Project Structure

```sh
└── tic_tac_toe/
    ├── __pycache__
    │   └── ai.cpython-313.pyc
    ├── ai.py
    ├── app.py
    ├── static
    │   ├── Codsoft task 1.mp4
    │   └── style.css
    └── templates
        └── index.html
```

---

### Project Index

<details open>
	<summary><b><code>TIC_TAC_TOE/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mommy15/tic_tac_toe/blob/master/app.py'>app.py</a></b></td>
					<td style='padding: 8px;'>- Provides the core web server for a Tic-Tac-Toe application, enabling user interaction through a web interface<br>- Handles rendering the main page and processing move requests by integrating AI logic to determine optimal moves<br>- Facilitates seamless communication between the frontend and AI module, supporting real-time gameplay within the overall application architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mommy15/tic_tac_toe/blob/master/ai.py'>ai.py</a></b></td>
					<td style='padding: 8px;'>- Implements an AI-powered decision engine for a Tic-Tac-Toe game, enabling optimal move selection through the minimax algorithm with alpha-beta pruning<br>- It evaluates game states to determine the best possible move for the computer opponent, ensuring challenging gameplay and strategic decision-making within the overall game architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- templates Submodule -->
	<details>
		<summary><b>templates</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ templates</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mommy15/tic_tac_toe/blob/master/templates/index.html'>index.html</a></b></td>
					<td style='padding: 8px;'>- Facilitates an interactive web interface for playing Tic-Tac-Toe against an AI opponent<br>- Manages user interactions, updates game state visually, and communicates with the backend to determine AI moves<br>- Ensures seamless gameplay flow, handles game over conditions, and provides options to reset the game, integrating frontend controls with server-side logic within the overall application architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Conda

### Installation

Build tic_tac_toe from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/mommy15/tic_tac_toe
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd tic_tac_toe
    ```

3. **Install the dependencies:**

**Using [conda](https://docs.conda.io/):**

```sh
❯ conda env create -f conda.yml
```

### Usage

Run the project with:

**Using [conda](https://docs.conda.io/):**

```sh
conda activate {venv}
python {entrypoint}
```

### Testing

Tic_tac_toe uses the {__test_framework__} test framework. Run the test suite with:

**Using [conda](https://docs.conda.io/):**

```sh
conda activate {venv}
pytest
```

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

<div align="left"><a href="#top">⬆ Return</a></div>

---
### 🎥 Demo Video

<video width="600" controls>
  <source src="static/output.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

