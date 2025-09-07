import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

def train_model(train_data_path):
    df = pd.read_csv(train_data_path)
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    X = df[features]
    y = df['Survived']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    dump(model, "model.joblib")
    preds = model.predict(X)
    acc = accuracy_score(y, preds)
    print(f"Training accuracy: {acc:.3f}")

if __name__ == "__main__":
    train_model("data/train_processed.csv")