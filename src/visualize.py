import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_survival(train_data_path):
    df = pd.read_csv(train_data_path)
    sns.countplot(x="Survived", data=df)
    plt.title("Survival Counts")
    plt.savefig("outputs/survival_counts.png")
    plt.close()

if __name__ == "__main__":
    plot_survival("data/train_processed.csv")