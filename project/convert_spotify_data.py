import pandas as pd

# this script has to be run before the "clean_spotify_dataset.ipynb" notebook.
# Please make sure you adapt the path before running this script.
def main():
    data = pd.read_csv("../data/charts.csv", engine = "c")
    data['date'] = pd.to_datetime(data['date'])
    truncated = data[(data['date'] > '2019-12-31')]
    truncated = truncated.drop(labels=["url"],axis=1)

    truncated.to_csv("../data/spotify_2020+.csv", index=False)

if __name__ == "__main__":
   main()