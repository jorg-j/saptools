# saptools
Python SAP integration. Conversion from VBS to Py

SAPConverter will take VBS recorded through SAP's built in GUI recorder and convert it into Python compatible code.
Run the program open the file you want to convert and the output file will contain code you can drag and drop into your project.

saptools handles the connection to SAP.
Connection defaults to session 0.
To connect to other sessions of SAP send session number as Argument:

Session 0
session = saptools.SAPConnect()

Session 1
session = saptools.SAPConnect(1)


