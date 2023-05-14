import sys
import os
from src.Exception import customException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifact','preprocessor.pkl')
            model_path=os.path.join('artifact','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise customException(e,sys)
        
class CustomData:
    def __init__(self,
                 Open:float,
                 High:float,
                 Low:float,
                 Close:float,
                 Volume:float,
                 Market_Cap:float,
                 Tomorrow:float,
                 ):
        
        self.Open=Open
        self.High=High
        self.Low=Low
        self.Close=Close	
        self.Volume=Volume
        self.Market_Cap=Market_Cap
        self.Tomorrow = Tomorrow
        

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Open':[self.Open],
                'High':[self.High],
                'Low':[self.Low],
                'Close':[self.Close],
                'Volume':[self.Volume],
                'Market_Cap':[self.Market_Cap],
                'Tomorrow':[self.Tomorrow]
                
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise customException(e,sys)
