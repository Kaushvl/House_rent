import os,sys
from src.exception import CustomException 
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:
    train_file_path = os.path.join("artifacts","train.csv")
    test_file_path = os.path.join("artifacts","test.csv")
    raw_file_path = os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enterd the data ingestion component")
        try:
            df=pd.read_csv("data\house_rent.csv")
            logging.info("Read data as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_file_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_file_path,header=True,index=False)

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_file_path,header=True,index=False)

            test_set.to_csv(self.ingestion_config.test_file_path,header=True,index=False)

            logging.info("data ingestion is completed")

            return(
                self.ingestion_config.train_file_path,
                self.ingestion_config.test_file_path
            )

        except Exception as e:
            return CustomException(e,sys)
        

if __name__=="__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    
    obj = DataTransformation()
    obj.initiate_data_transformation(train_data,test_data)