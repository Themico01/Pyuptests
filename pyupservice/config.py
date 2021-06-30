from pyupservice.client_config import ClientConfig

CLIENT_CONFIG=ClientConfig()

def UpdatePyUpdaterClientConfig(clientConfig):
    """
    Update PyUpdater client config.
    This is the configuration (sometimes stored in client_config.py)
    which tells the application where to look for updates.

    The main role of this method to set the UPDATE_URLS in the
    client config. 
    """
    
   
    CLIENT_CONFIG.APP_NAME = clientConfig.APP_NAME
    CLIENT_CONFIG.COMPANY_NAME = clientConfig.COMPANY_NAME
    CLIENT_CONFIG.MAX_DOWNLOAD_RETRIES = clientConfig.MAX_DOWNLOAD_RETRIES
    CLIENT_CONFIG.PUBLIC_KEY = clientConfig.PUBLIC_KEY
    CLIENT_CONFIG.UPDATE_URLS =clientConfig.UPDATE_URLS
    
    return CLIENT_CONFIG
