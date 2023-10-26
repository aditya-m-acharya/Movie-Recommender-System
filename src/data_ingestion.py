from src import config_entity
from pathlib import Path
import pandas as pd

class DataIngestion:
    def load_data():
        config = config_entity.ConfigFile.parse_config(config_entity.CONFIG_FILE)
        movies_data = Path(config["data_ingestion"]["movies_data"])
        users_data = Path(config["data_ingestion"]["users_data"])
        ratings_data = Path(config["data_ingestion"]["ratings_data"])
        movies = pd.read_fwf(movies_data, encoding='ISO-8859-1')
        users = pd.read_fwf(users_data, encoding='ISO-8859-1')
        ratings = pd.read_fwf(ratings_data, encoding='ISO-8859-1')
        return movies, users, ratings