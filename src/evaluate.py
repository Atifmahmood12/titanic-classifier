import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Paths to validation features and labels (from train.py)
features_path = 'data/features.csv'
labels_path = 'data/labels.csv'
model_path = 'data/model.joblib'

import joblib

def evaluate_model():
    # Load validation data
    X_val = pd.read_csv(features_path)
    y_val = pd.read_csv(labels_path).squeeze()  # Squeeze to get a Series

    # Load trained model
    clf = joblib.load(model_path)

    # Predict
    y_pred = clf.predict(X_val)

    # Metrics
    acc = accuracy_score(y_val, y_pred)
    prec = precision_score(y_val, y_pred)
    rec = recall_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred)
    cm = confusion_matrix(y_val, y_pred)

    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print("Confusion Matrix:")
    print(cm)

if __name__ == "__main__":
    evaluate_model()
