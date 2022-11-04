import pandas as pd




def main():
    data = pd.read_csv("data/charts.csv", engine = "c")
    data['date'] = pd.to_datetime(data['date'])
    truncated = data[(data['date'] > '2019-12-31')]
    truncated = truncated.drop(labels=["url"],axis=1)

    truncated.to_csv("data/spotify_2020+.csv")













if __name__ == "__main__":
   main()