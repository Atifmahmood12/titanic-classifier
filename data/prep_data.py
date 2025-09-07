import pandas as pd

def load_and_clean_data(path='data/titanic.csv'):
    df = pd.read_csv(path)
    # Basic cleaning: fill missing, encode categorical
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna('S', inplace=True)
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    features = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
    labels = df['Survived']
    return features, labels

if __name__ == "__main__":
    X, y = load_and_clean_data()
    X.to_csv('data/features.csv', index=False)
    y.to_csv('data/labels.csv', index=False)
    print("Data prepped and saved to data/features.csv and data/labels.csv")