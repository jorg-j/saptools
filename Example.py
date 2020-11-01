'''
Opens T-Code VA01
'''

import sys
import saptools

# Connection to SAP
session = saptools.SAPConnect()

try:
    session.findById("wnd[0]").maximize() # SAP Session is Maximised
    session.findById("wnd[0]/tbar[0]/okcd").text = "/nVA01" # Key T-Code to toolbar
    session.findById("wnd[0]").sendVKey (0) # Press Enter
except:
    print(sys.exc_info()[0])
