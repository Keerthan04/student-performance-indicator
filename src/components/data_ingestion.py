#read the data from the data source,split the data to train and split and then goes to data transformation
import os
import sys
from src.exception import customException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

#there will be like the input component and all to tell where to store and all for that can use class 
@dataclass#decorator allows to create as variable
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()#all 3 variables will get stored in this ingestion part
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            #reading of dataset logic is written here
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as a dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)#exists ok to tell if already there leave it as it is 
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Train Test Split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
                #so that for the data transformation we can do
            )
        except Exception as e:
            logging.error(f"Error in the data ingestion component:{str(e)}")
            raise customException(e,sys)

if __name__ == "__main__":
    data_ingestion=DataIngestion()
    train_data,test_data,_ = data_ingestion.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)
    
    modelTrainer = ModelTrainer()
    print(modelTrainer.initiate_model_trainer(train_array=train_arr,test_array=test_arr))