import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(path='data/train.csv'):
    df = pd.read_csv(path)
    # Example: Survival rate by class
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Pclass', y='Survived', data=df)
    plt.title('Survival Rate by Passenger Class')
    plt.ylabel('Survival Rate')
    plt.xlabel('Passenger Class')
    plt.tight_layout()
    plt.show()

    # Example: Age distribution
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Age'].dropna(), bins=20, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_data()