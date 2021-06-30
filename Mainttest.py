import requests

from pyupservice.client_config import ClientConfig



def testupdate():
    
    "Carga la configuración de cliente"
    CLIENT_CONFIG=ClientConfig()
    print(CLIENT_CONFIG.APP_NAME)
    print(CLIENT_CONFIG.UPDATE_URLS)
    
    "Comprobar si hay conexión con un servidor"
    

if __name__ == "__main__": 
    testupdate()
