import sys
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import os
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprecessor_obj_file_path =os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformatio_config =DataTransformationConfig()

    def get_data_transformation_object(self):

        try:
            numerical_columns =['writing_score','reading_score']
            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education' ,
                'lunch',
                'test_preparation_course']
            numerical_pipeline = Pipeline(
                steps =[
                ("imputer", SimpleImputer(strategy='median'))
                ("scaler", StandardScaler)
            ])

            cat_pipeline= Pipeline(

                steps =[
                ('imputer', SimpleImputer(strategy='mode'))
                ("one hot encoder", OneHotEncoder)
                ('scaler', StandardScaler)
                ])
            
            logging.info('Numerical columns scaling completed')

            logging.info('categorical columns encoding completed')

            preprocessor = ColumnTransformer(

                [
                ('numerical_pipeline',numerical_pipeline, numerical_columns)
                ('cat_pipeline', cat_pipeline, categorical_columns)


                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
            

    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('reading train and test is completed')

            logging.info('obtainig preprocessor object')

            preprocessing_obj = self.get_data_transformation_object()
            target_column_name = "math_score"
            numerical_columns = ['writing_score','reading_score']

            input_feature_traindf= train_df.drop(target_column_name, axis=1)




        except:
            pass       

        


