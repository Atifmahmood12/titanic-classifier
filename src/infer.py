import pandas as pd
from joblib import load

def run_inference(test_data_path, model_path):
    df = pd.read_csv(test_data_path)
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    X = df[features]
    model = load(model_path)
    preds = model.predict(X)
    df['Prediction'] = preds
    df.to_csv("data/test_predictions.csv", index=False)
    print("Predictions saved to data/test_predictions.csv")

if __name__ == "__main__":
    run_inference("data/test_processed.csv", "model.joblib")
