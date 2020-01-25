'''
Useage: Global Module
Author: jorg-j
https://github.com/jorg-j/
Date: 25-01-2020

Dependencies:
    pywin32
'''

import os
import time
import sys
import win32com.client
import datetime
import json
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='app.log',filemode='a',level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Starting saptools')

#-----------------------------------------------------------------------

############################ Configuration #############################

try:
    with open('config.json') as json_file:
        Config = json.load(json_file)
        logger.info('Config Imported')
except:
    Config = {}
    logger.warning('No Config Found')


#-----------------------------------------------------------------------

############################# Connection ###############################

def SAPConnect():
    try:
        logger.info('Connecting to SAP')
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
        connection = application.Children(0)
        if not type(application) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
        session = connection.Children(0)  # set session 1 of SAP
        if not type(application) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
        logger.info('SAP Connected')
        return session

    except:
        print(sys.exc_info()[0])
        logger.critical('SAP Connection Failed')
        return "fault"
