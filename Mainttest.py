


from pyupservice.client_config import ClientConfig
from pyupservice.fileserver import WaitForFileServerToStart


CLIENT_CONFIG=ClientConfig()

def CheckForUpdates(fileServerPort, debug):
    """
    Check for updates.
    Channel options are stable, beta & alpha
    Patches are only created & applied on the stable channel
    """
    assert CLIENT_CONFIG.PUBLIC_KEY is not None
    client = Client (CLIENT_CONFIG, refresh=True)
    appUpdate = client.update_check(CLIENT_CONFIG.APP_NAME,
                                    wxupdatedemo.__version__,
                                    channel='stable')
    if appUpdate:
        if hasattr(sys, "frozen"):
            downloaded = appUpdate.download()
            if downloaded:
                status = UpdateStatus.EXTRACTING_UPDATE_AND_RESTARTING
                ShutDownFileServer(fileServerPort)
                if debug:
                    logger.debug('Extracting update and restarting...')
                    time.sleep(10)
                appUpdate.extract_restart()
            else:
                status = UpdateStatus.UPDATE_DOWNLOAD_FAILED
        else:
            status = UpdateStatus.UPDATE_AVAILABLE_BUT_APP_NOT_FROZEN
    else:
        status = UpdateStatus.NO_AVAILABLE_UPDATES
    return status





def testupdate():
    
    "Carga la configuración de cliente"
    print(CLIENT_CONFIG.APP_NAME)
    print(CLIENT_CONFIG.UPDATE_URLS[0])
    url=CLIENT_CONFIG.UPDATE_URLS[0]
    timeout=CLIENT_CONFIG.HTTP_TIMEOUT
    
    "Comprobar si hay conexión con un servidor"
    connectionstatus=WaitForFileServerToStart(url,timeout)
    if connectionstatus != None:
        print(connectionstatus)
    else:
        print('No ha habido éxito')
        
    
    
    

if __name__ == "__main__": 
    testupdate()
