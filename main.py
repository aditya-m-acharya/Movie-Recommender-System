from src import data_ingestion

if __name__== "__main__":
    movies, users, ratings = data_ingestion.DataIngestion.load_data()
    print(movies.head())