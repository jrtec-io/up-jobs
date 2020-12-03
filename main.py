import os
from dotenv import load_dotenv
from pprint import pprint
import upwork


if __name__ == "__main__":
    ## Read environment varibales
    load_dotenv()
    public_key = os.environ.get('KEY') 
    secret_key = os.environ.get('SECRET') 

    ## Login to api account
    client = None
    try:
        client = upwork.Client(public_key, secret_key)
        print(client.auth.get_info())
        #pprint(client)
        pass
    except Exception as error:
        print('error: ', error)
        pass
    finally:
        print('everything ok')
        pass


    pass