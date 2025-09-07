import pandas as pd

def load_data(train_path, test_path):
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df

def preprocess(df):
    df = df.copy()
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    df['Embarked'] = df['Embarked'].fillna('S')
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    return df

if __name__ == "__main__":
    train_df, test_df = load_data("data/raw_train.csv", "data/test.csv")
    train_df = preprocess(train_df)
    test_df = preprocess(test_df)
    train_df.to_csv("data/train_processed.csv", index=False)
    test_df.to_csv("data/test_processed.csv", index=False)