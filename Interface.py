from tkinter import *

from Mainttest import testupdate
from pyupservice.client_config import ClientConfig



version="0.0.2"
CLIENT_CONFIG=ClientConfig()

class Application:
   
    def __init__(self,window):
            
            self.wind=window
            
            login=LabelFrame(self.wind, text = 'Login')
            login.grid(row = 0, column = 0, columnspan = 2)
            
            Label(login,text='Version: ').grid(row=0,column=0)
            Label(login,text=version).grid(row=0,column=1)
            
            
            
if __name__=='__main__':
    testupdate(CLIENT_CONFIG,version)
    window=Tk()
    application=Application(window)
    window.mainloop() 


