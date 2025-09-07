import pandas as pd
import joblib

def run_inference(input_path='data/test.csv', output_path='data/predictions.csv'):
    # Load test data
    test_df = pd.read_csv(input_path)
    # Example feature selection and preprocessing (modify as needed)
    X_test = test_df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
    X_test = pd.get_dummies(X_test, columns=['Sex'])
    X_test = X_test.fillna(X_test.median())

    # Load trained model
    clf = joblib.load('data/model.joblib')

    # Predict
    preds = clf.predict(X_test)
    test_df['Predicted'] = preds

    # Save predictions
    test_df.to_csv(output_path, index=False)
    print(f"Inference complete. Predictions saved to {output_path}")

if __name__ == "__main__":
    run_inference()