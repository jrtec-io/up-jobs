import os
from dotenv import load_dotenv
import upwork



if __name__ == "__main__":
    ## Read environment varibales
    load_dotenv()
    key = os.environ.get('KEY') 
    secret = os.environ.get('SECRET') 


    print(key)
    print(secret)
    pass