from src import data_ingestion, data_transformation, model_trainer, model_recommender

if __name__== "__main__":
    movies, users, ratings = data_ingestion.DataIngestion.load_data()
    movies, users, ratings = data_ingestion.DataIngestion.data_cleaning(movies, users, ratings)
    users = data_transformation.DataTransformation.num_to_cat(users)
    print(movies.info())
    data = data_transformation.DataTransformation.data_preparation(movies, users, ratings)
    data = data_transformation.DataTransformation.feature_engineering(data)
    user_itm, rm = data_transformation.DataTransformation.data_model_preprocess(data)
    #print(user_itm.info())
    model_trainer.ModelTrainer.recommendation_model(user_itm, rm)
    top_items = model_recommender.Model_Predictor.make_predictions('1', 10, movies)
    print(top_items)