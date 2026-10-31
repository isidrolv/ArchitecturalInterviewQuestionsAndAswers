# Self-Test App

Python tools for practicing the software architecture interview questions from
[`../README.md`](../README.md), based on the question bank in
[`../architectural-interview-questions.json`](../architectural-interview-questions.json).

## Prerequisites

```bash
pip install pyyaml matplotlib
```

> `tkinter` is required for the GUI app and ships with most Python distributions.
> Install it via your OS package manager if it is missing (e.g. `sudo apt install python3-tk`).

## Scripts

| Script | Description |
|---|---|
| `architecture_quiz_console.py` | Terminal-based interactive quiz, shows a results chart at the end |
| `architecture_quiz_gui.py` | Graphical quiz (tkinter): full quiz, quick quiz, custom quiz, filter by level/category, study mode |

## Usage

Run both scripts from **any** working directory; they resolve paths relative to their own location.

### Console quiz

```bash
python self-test-app/architecture_quiz_console.py
```

### GUI quiz

```bash
python self-test-app/architecture_quiz_gui.py
```

## Configuration

Edit `self-test-app/config.yml` to adjust the pass threshold and the maximum number of
questions shown per session in the console quiz.

## Data

`architectural-interview-questions.json` (project root) — the question bank used by both quiz apps.
Answers are evenly distributed across options `a`/`b`/`c`/`d` (15 each) to avoid guessable patterns.
