import sys
import saptools

session = saptools.SAPConnect()

try:
    session.findById("wnd[0]").maximize()
    session.findById("wnd[0]/tbar[0]/okcd").text = "/nVA01"
    session.findById("wnd[0]").sendVKey (0)
except:
    print(sys.exc_info()[0])