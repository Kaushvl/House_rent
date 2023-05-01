import sys,os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(features)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        BHK: int,
        Size: int,
        Floor: int,
        Area_Type: int,
        City:int,
        Furnishing_Status: int,
        Tenant_Preferred: int,
        Bathroom:int):

        self.BHK = BHK

        self.Size = Size

        self.Floor = Floor

        self.Area_Type = Area_Type

        self.City = City

        self.Furnishing_Status = Furnishing_Status

        self.Tenant_Preferred = Tenant_Preferred

        self.Bathroom = Bathroom

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "BHK": [self.BHK],
                "Size": [self.Size],
                "Floor": [self.Floor],
                "Area_Type": [self.Area_Type],
                "City" : [self.City],
                "Furnishing_Status": [self.Furnishing_Status],
                "Tenant_Preferred": [self.Tenant_Preferred],
                "Bathroom": [self.Bathroom],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)