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
    
    def data_cleaning(movies, users, ratings):
        movies.drop(columns=['Unnamed: 1', 'Unnamed: 2'], axis=1, inplace=True)
        delimiter = '::'
        movies = movies['Movie ID::Title::Genres'].str.split(delimiter, expand=True)
        movies.columns = ['Movie ID', 'Title', 'Genres']
        movies.rename(columns={'Movie ID':'MovieID'}, inplace=True)
        ratings = ratings['UserID::MovieID::Rating::Timestamp'].str.split(delimiter, expand=True)
        ratings.columns = ['UserID', 'MovieID', 'Rating', 'Timestamp']
        users = users['UserID::Gender::Age::Occupation::Zip-code'].str.split(delimiter, expand=True)
        users.columns = ['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code']
        return movies, users, ratings