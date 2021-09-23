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

import sys

import win32com.client


# -----------------------------------------------------------------------

############################# Connection ###############################


def SAP_connect(SessionID=0):
    """
    Manages connection between Py and SAP
    """

    try:
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
        return session
    except:
        print(sys.exc_info()[0])
        return "Disconnected"
