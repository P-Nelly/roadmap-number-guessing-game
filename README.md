<div align="left" style="position: relative;">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>ROADMAP-NUMBER-GUESSING-GAME</h1>
<p align="left">
	<em><code>❯ A classic number guessing game with multiple difficulty levels and high scores</code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/P-Nelly/roadmap-number-guessing-game?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/P-Nelly/roadmap-number-guessing-game?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/P-Nelly/roadmap-number-guessing-game?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/P-Nelly/roadmap-number-guessing-game?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

##  Table of Contents

- [ Overview](#overview)
- [ Features](#features)
- [ Project Structure](#project-structure)
  - [ Project Index](#project-index)
- [ Getting Started](#getting-started)
  - [ Prerequisites](#prerequisites)
  - [ Installation](#installation)
  - [ Usage](#usage)
  - [ Testing](#testing)
- [ Project Roadmap](#project-roadmap)
- [ Contributing](#contributing)
- [ License](#license)
- [ Acknowledgments](#acknowledgments)

---

##  Overview

A classic number guessing game implemented in Python where players try to guess a randomly generated number between 1 and 100. The game features multiple difficulty levels, hints, and a high score system.

---

##  Features

- Three difficulty levels: Easy (10 attempts), Medium (5 attempts), and Hard (3 attempts)
- Dynamic feedback on each guess (higher/lower hints)
- High score tracking for each difficulty level
- Time tracking for each game round
- Input validation and error handling
- User-friendly command-line interface

---

##  Project Structure

```sh
└── roadmap-number-guessing-game/
    ├── LICENSE
    ├── README.md
    └── main.py
```


###  Project Index
<details open>
	<summary><b><code>ROADMAP-NUMBER-GUESSING-GAME/</code></b></summary>
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-number-guessing-game/blob/master/main.py'>main.py</a></b></td>
				<td>Main game implementation containing the NumberGuessingGame class and game logic</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-number-guessing-game/blob/master/README.md'>README.md</a></b></td>
				<td>Project documentation and setup instructions</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with roadmap-number-guessing-game, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python


###  Installation

Install roadmap-number-guessing-game using one of the following methods:

**Build from source:**

1. Clone the roadmap-number-guessing-game repository:
```sh
❯ git clone https://github.com/P-Nelly/roadmap-number-guessing-game
```

2. Navigate to the project directory:
```sh
❯ cd roadmap-number-guessing-game
```

3. No additional dependencies required! The game uses only Python standard library.

###  Usage
Run the game using the following command:
```sh
❯ python main.py
```

###  Testing
No formal testing suite is implemented yet. Manual testing can be performed by running the game and trying different inputs.

---
##  Project Roadmap

- [X] **`Task 1`**: Implement basic number guessing game functionality
- [ ] **`Task 2`**: Add persistent high scores using file storage
- [ ] **`Task 3`**: Implement a graphical user interface
- [ ] **`Task 4`**: Add additional game modes and features
- [ ] **`Task 5`**: Create a multiplayer mode

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/P-Nelly/roadmap-number-guessing-game/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/P-Nelly/roadmap-number-guessing-game/issues)**: Submit bugs found or log feature requests for the `roadmap-number-guessing-game` project.
- **💡 [Submit Pull Requests](https://github.com/P-Nelly/roadmap-number-guessing-game/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/P-Nelly/roadmap-number-guessing-game
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/P-Nelly/roadmap-number-guessing-game/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=P-Nelly/roadmap-number-guessing-game">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/). For more details, refer to the [LICENSE](LICENSE) file.

---

##  Acknowledgments

- Built as part of the Python learning roadmap: https://roadmap.sh/projects/number-guessing-game
- Inspired by classic number guessing games
- Uses Python's random and time modules from the standard library

---
