import pandas as pd
import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    # Load your dataset
    df = pd.read_csv('data/train.csv', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Example feature selection - modify as needed!
    X = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
    # Convert categorical columns
    X = pd.get_dummies(X, columns=['Sex'])
    y = df['Survived']
    
    # Fill missing values (simple strategy)
    X = X.fillna(X.median())

    # Split for validation (optional)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Save model
    joblib.dump(clf, 'data/model.joblib')
    # Also save validation set for evaluation
    X_val.to_csv('data/features.csv', index=False)
    pd.DataFrame(y_val).to_csv('data/labels.csv', index=False)
    print("Training complete and model saved!")

if __name__ == "__main__":
    train_model()