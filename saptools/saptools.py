#!/usr/bin/python3
"""
Useage: Global Module
Author: jorg-j
https://github.com/jorg-j/
Date: 2020-11-17

Dependencies:
    pywin32

Currently Tested on SAP GUI 7
"""


import logging
import sys

import win32com.client

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="SAP.log",
    filemode="a",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
logger.info("Starting saptools")


# -----------------------------------------------------------------------

############################# Connection ###############################


def SAPConnect(SessionID=0):
    """
    Manages connection between Py and SAP
    """

    try:
        logger.info("Connecting to SAP")
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
        connection = application.Children(0)
        if not type(application) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
        session = connection.Children(SessionID)  # set session 1 of SAP
        if not type(application) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
        logger.info("SAP Connected")
        return session

    except:
        print(sys.exc_info()[0])
        logger.critical("SAP Connection Failed")
        return "Disconnected"
