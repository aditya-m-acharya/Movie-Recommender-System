from cmfrec import CMF
import numpy as np
#from sklearn.metrics import mean_absolute_percentage_error
#from sklearn.metrics import mean_squared_error
from src import config_entity
config = config_entity.ConfigFile.parse_config(config_entity.CONFIG_FILE)
from pathlib import Path

from pickle import dump

class ModelTrainer:
    def recommendation_model(user_itm, rm):
        #x = [2,4,6,8]
        #rmse_mat = []
        #mape_mat = []
        #for k in x:
        model = CMF(method="als", k=2, lambda_=0.1, user_bias=False, item_bias=False, verbose=False) 
        model.fit(user_itm)
        #rm__ = np.dot(model.A_, model.B_.T) + model.glob_mean_ #Calculating the predicted ratings
        #rmse = mean_squared_error(rm.values[rm > 0], rm__[rm > 0], squared=False) # calculating rmse value
        #rmse_mat.append(rmse)
        #mape =  mean_absolute_percentage_error(rm.values[rm > 0], rm__[rm > 0]) #calculating mape value
        #mape_mat.append(mape)
        #return rmse, mape
        model_path = Path(config["model_trainer"]["model_path"])
        model_path.parent.mkdir(parents=True, exist_ok=True)
        dump(model, open(model_path, "wb"))