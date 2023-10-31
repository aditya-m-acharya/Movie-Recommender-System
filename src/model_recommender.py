from pickle import load
from src import config_entity
config = config_entity.ConfigFile.parse_config(config_entity.CONFIG_FILE)
from pathlib import Path
import pandas as pd

import numpy as np

class Model_Predictor:
    def make_predictions(user, no_of_recommendations, movies_df):
        model_path = Path(config["model_trainer"]["model_path"])
        rec_trained_model = load(open(model_path, "rb"))
        top_items = rec_trained_model.topN(user=user, n=no_of_recommendations)
        movies_df.set_index('MovieID', inplace=True, drop=True)
        return movies_df.loc[top_items.astype('str')]