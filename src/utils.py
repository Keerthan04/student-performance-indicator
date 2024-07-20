#will have common functionalities which entire project can use
import os
import sys

import numpy as np
import pandas as pd

from src.exception import customException
from src.logger import logging
import dill

def save_object(file_path,obj):
    '''
    This function is responsible to save the object
    '''
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)#dill for saving the pickle file
            
    except Exception as e:
        logging.error(f"Error in saving the object: {e}")
        raise customException(e,sys)