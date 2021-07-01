
import sys
import time

from tkinter import *
from tkinter import messagebox
from pyupdater.client import Client
from pyupservice.fileserver import WaitForFileServerToStart



class UpdateStatus():
    """Enumerated data type"""
    UNKNOWN = 0
    NO_AVAILABLE_UPDATES = 1
    UPDATE_DOWNLOAD_FAILED = 2
    EXTRACTING_UPDATE_AND_RESTARTING = 3
    UPDATE_AVAILABLE_BUT_APP_NOT_FROZEN = 4
    COULDNT_CHECK_FOR_UPDATES = 5

UPDATE_STATUS_STR = \
    ['Unknown', 'No available updates were found.',
     'Update download failed.', 'Extracting update and restarting.',
     'Update available but application is not frozen.',
     'Couldn\'t check for updates.']

"Función que comprueba so hay actualizaciones, la descarga y la instala"
def CheckForUpdates(CLIENT_CONFIG,version):
    """
    Check for updates.
    Channel options are stable, beta & alpha
    Patches are only created & applied on the stable channel
    """
    "Inicializa un cliente"
    client = Client (CLIENT_CONFIG, refresh=True)
    
    "Comprueba si hay alguna actualización"
    appUpdate = client.update_check(CLIENT_CONFIG.APP_NAME,version,channel='stable')
    
    if appUpdate:
        "Comprueba si el script forma parte de un bundle o es independiente"
        if hasattr(sys, "frozen"):
            "Descarga el update"
            downloaded = appUpdate.download()
            if downloaded:
                status = UpdateStatus.EXTRACTING_UPDATE_AND_RESTARTING
                statusmessage=UPDATE_STATUS_STR[status]
                messagebox.showinfo("Status",statusmessage)
                appUpdate.extract_restart()
            else:
                status = UpdateStatus.UPDATE_DOWNLOAD_FAILED
        else:
            status = UpdateStatus.UPDATE_AVAILABLE_BUT_APP_NOT_FROZEN
    else:
        status = 0
    if status is not 0:
        statusmessage=UPDATE_STATUS_STR[status]
        messagebox.showinfo("Status",statusmessage)


def testupdate(CLIENT_CONFIG,version):
    
    "Carga la configuración de cliente"
    url=CLIENT_CONFIG.UPDATE_URLS[0]
    timeout=CLIENT_CONFIG.HTTP_TIMEOUT
    
    "Comprobar si hay conexión con un servidor"
    connectionstatus=WaitForFileServerToStart(url,timeout)
    
    if connectionstatus:
        if connectionstatus == 404:
            status=UpdateStatus.COULDNT_CHECK_FOR_UPDATES
            statusmessage=UPDATE_STATUS_STR[status]
            messagebox.showinfo("Status",statusmessage)        
        else:
            status=CheckForUpdates(CLIENT_CONFIG,version)

    else: 
        status=UpdateStatus.COULDNT_CHECK_FOR_UPDATES
        statusmessage=UPDATE_STATUS_STR[status]
        messagebox.showinfo("Status",statusmessage)  
    
    
      
        
       
