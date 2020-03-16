import pickle
import pandas as pd

from data_handling.pipeline import *


def test_data(model_filepath,  csv_filepath, needs_cleaning=False):
    # read in file
    df = pd.read_csv(csv_filepath)
    if needs_cleaning:
        # clean the dataframe
        df = clean_data(df)
    with open(model_filepath, 'rb') as file:
        clf = pickle.load(file)
    x, y = get_xy(df)
    score = clf.score(x, y)
    print("Data Was Scored By Model")
    print(f"Accuracy = {score}")
    return None


if __name__=="__main__":
    model_filepath = "./models/rf_bc.pkl"
    csv_filepath="./data/df_cleaned.csv"
    test_data(model_filepath=model_filepath,
              csv_filepath=csv_filepath)