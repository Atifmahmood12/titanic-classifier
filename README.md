# Titanic Classifier ML Project

## Overview

This project builds a simple ML classifier (Logistic Regression) to predict Titanic survival. It demonstrates good project architecture for data, code, notebooks, automation, and documentation.

## Structure

- `data/`: Titanic dataset & processed files
- `notebooks/`: Jupyter notebooks for EDA
- `src/`: Python scripts for data prep, training, evaluation
- `.github/workflows/ci.yml`: GitHub Actions for CI/CD
- `requirements.txt`: Dependencies

## How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/Atifmahmood12/titanic-classifier.git
   cd titanic-classifier
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare data**
   - Place Titanic CSV in `data/titanic.csv`
   - Or use `notebooks/exploratory.ipynb` for EDA

4. **Run scripts**
   ```bash
   python src/data_prep.py
   python src/train.py
   python src/evaluate.py
   ```

5. **Automation**
   - On every push/PR, GitHub Actions runs the pipeline (`.github/workflows/ci.yml`).

## Architecture

```
data/            # raw and processed data
notebooks/       # analysis notebooks
src/             # main scripts
.github/         # CI/CD workflow
requirements.txt # dependencies
README.md        # instructions
```

## How GitHub Actions Work

On push/PR, GitHub CI will:
- Set up Python
- Install dependencies
- Run data prep, training, evaluation scripts

## Experimenting in VS Code

- Open the repo in VS Code for code, notebooks, and automation.
- Use the built-in terminal to run scripts.
- Use extensions for Python, Jupyter, and GitHub for seamless workflow.

---

**Happy experimenting!**