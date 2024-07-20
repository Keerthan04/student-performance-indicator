#sys provides info of exception and all
import sys
#from src.logger import logging if to log inside in exception 

def error_message_detail(error,error_detail:sys):
	# add an indented block of code here
    _,_,exc_tb = error_detail.exc_info()#exc_tb will give us all the info like of all the exception and all those stuff
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
    
class customException(Exception):#inheriting the parent exception
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)#passing to the exception class
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
