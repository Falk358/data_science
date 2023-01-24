# Guide: Spotify chart prediction

**NOTE:** We did not continue our work with the Billboard dataset for the prediction of ranks in the charts. Files, which we submitted at an earlier milestone, are not included in this final hand-in. These files include:
- dataset `billboardCharts.csv`
- cleaning of the data `01_clean_billboard_charts_dataset.ipynb`

For this project, multiple files are used. This file is a guideline on how to execute the different parts and how to execute everything.

Every major task has its respective file. We split the tasks up in:
1. cleaning the data: `01_clean_spotify_dataset.ipynb`
2. apply exploratory analysis: `02_exploratory_data_analysis.ipynb`
3. prediction: `03_prediction.ipynb`
4. hypothesis testing: `04_hypothesis_testing.ipynb`

The dataset:
- `charts.csv` (source: https://www.kaggle.com/datasets/dhruvildave/spotify-charts)

Because we have a rather big dataset, we first need to do some preparation for later processing of the data. This is done in `convert_spotify_data.py` and the execution of this script returns a more usable dataset with the name `spotify_2020+.csv`. We simply removed dates before 2022.

Every task is producing a new csv, which will be imported for the following task. In detail:
1. Task exports to `spotify_2020+_cleaned.csv`
2. Task has one export for every approach we used
  * approach 1: `viral50_to_top200.csv`
  * approach 2: `viral50_and_trend_to_top200.csv`
  * approach 3: `weekly_ranks_top_200.csv` for weekly period, `3_days_ranks_top_200.csv` for three days period and `daily_ranks_top_200.csv` for daily period
3. Task also has one export per approach
  * approach 1: `classification_results_approach_1.csv`
  * approach 2: `classification_results_approach_2.csv`
  * approach 3: `classification_results_approach_3.csv`
4. Task has no export since it is the last notebook of our project

So, in a nutshell, every major task can be executed one after the other.