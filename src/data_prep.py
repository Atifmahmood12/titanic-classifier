import pandas as pd

def preprocess_data(input_path='data/raw_train.csv', output_path='data/train.csv'):
    # Load raw data
    df = pd.read_csv(input_path)

    # Example: Fill missing ages with median
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())

    # Example: Fill missing fares with median
    if 'Fare' in df.columns:
        df['Fare'] = df['Fare'].fillna(df['Fare'].median())

    # Example: Drop columns not needed for ML (modify as needed)
    drop_cols = ['Name', 'Ticket', 'Cabin']
    for col in drop_cols:
        if col in df.columns:
            df = df.drop(col, axis=1)

    # Save processed data
    df.to_csv(output_path, index=False)
    print(f"Data preprocessed and saved to {output_path}")

if __name__ == "__main__":
    preprocess_data()