## Running the Full Pipeline

To automate the entire workflow (data preprocessing, training, inference, evaluation, and visualization), use the provided pipeline script:

```bash
python run_pipeline.py
```

This script will:
- Clean up any previously generated output files
- Run all necessary scripts in sequence
- Ensure a fresh start for each run

You can modify the pipeline script to fit your custom workflow if needed.
# Titanic Classifier

This repository contains a simple machine learning pipeline for predicting survival on the Titanic dataset. It includes scripts for data preprocessing, model training, evaluation, inference, and visualization.

## Folder Structure

```
src/
  ├── data_prep.py      # Data preprocessing: cleans and prepares raw data
  ├── train.py          # Trains the model and saves it
  ├── evaluate.py       # Evaluates the trained model
  ├── infer.py          # Generates predictions on test data
  └── visualize.py      # Visualizes data and results
data/
  ├── raw_train.csv     # Raw training data (input for preprocessing)
  ├── train.csv         # Cleaned training data
  ├── test.csv          # Test data for inference
  ├── model.joblib      # Saved ML model
  ├── features.csv      # Validation features for evaluation
  ├── labels.csv        # Validation labels for evaluation
  └── predictions.csv   # Output predictions from inference
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Atifmahmood12/titanic-classifier.git
   cd titanic-classifier
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Sample Data

Sample data files (`raw_train.csv` and `test.csv`) should be placed in the `data/` directory.  
You can download public Titanic datasets from [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic/data) and rename them as follows:

- Training data: `data/raw_train.csv` (originally `train.csv` from Kaggle)
- Test data: `data/test.csv` (originally `test.csv` from Kaggle)

**Minimal Example of `data/raw_train.csv`:**
```csv
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
1,0,3,Braund, Mr. Owen Harris,male,22,1,0,A/5 21171,7.25,,S
2,1,1,Cumings, Mrs. John Bradley (Florence Briggs Thayer),female,38,1,0,PC 17599,71.2833,C85,C
3,1,3,Heikkinen, Miss. Laina,female,26,0,0,STON/O2. 3101282,7.925,,S
```

**Minimal Example of `data/test.csv`:**
```csv
PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
892,3,Kelly, Mr. James,male,34.5,0,0,330911,7.8292,,Q
893,3,Williams, Mr. Charles Eugene,male,47,0,0,363272,7,,S
894,2,Wilkes, Mrs. James (Ellen Needs),female,27,1,0,363951,13,,S
```

## Usage

   python src/data_prep.py
## How the Model is Trained

The Titanic survival model uses a Random Forest Classifier to learn patterns from passenger data. The process is:

1. **Feature Preparation:**
   - Selects columns: `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`.
   - Converts categorical columns (like `Sex`) to numeric using one-hot encoding (`get_dummies`).
2. **Model Training:**
   - The Random Forest algorithm builds many decision trees using the features and learns to predict the target (`Survived`).
3. **Validation:**
   - The data is split into training and validation sets to check model performance.
4. **Saving the Model:**
   - The trained model is saved for later inference.

### Visual Representation
Your features (after encoding with get_dummies) are fed into the Random Forest model.
The model learns relationships between features and the target (Survived).
After training, the model can predict survival for new passengers.
+-------------------+      +--------------------------+      +-------------------+
|   Features (X)    | ---> | RandomForestClassifier   | ---> |   Prediction (y)  |
|-------------------|      |--------------------------|      |-------------------|
| Pclass            |      |  - Builds many trees     |      | Survived: 0 or 1  |
| Sex_0, Sex_1      |      |  - Learns patterns       |      |                   |
| Age               |      |  - Combines votes        |      |                   |
| SibSp             |      |                          |      |                   |
| Parch             |      |                          |      |                   |
| Fare              |      |                          |      |                   |
| Embarked          |      |                          |      |                   |
+-------------------+      +--------------------------+      +-------------------+

```
+-------------------+      +--------------------------+      +-------------------+
   ```

2. **Train model**

   ```bash
   python src/train.py
   ```

3. **Evaluate model**
+-------------------+      +--------------------------+      +-------------------+


This diagram shows how passenger features are used to train the model, which then predicts survival.
   ```bash
   python src/evaluate.py
   ```

4. **Run inference**

   ```bash
   python src/infer.py
   ```

5. **Visualize data**

   ```bash
   python src/visualize.py
   ```

## Requirements

See `requirements.txt`.

## Notes

- Update feature selection as needed in each script to match your data.
- Place your raw train and test datasets in the `data/` folder as `raw_train.csv` and `test.csv`.
- The scripts assume basic preprocessing and feature engineering; modify as necessary for your project.

## License

MIT