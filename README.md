# saptools

Python SAP integration. 


## VBS Conversion

SAPConverter.py takes SAP GUI scripts and converts to drag and drop py.

Run SAPConverter.py open the file for conversion and outfile.py file will contain code you can drag and drop into your project.

## Connection to SAP

saptools.py handles the connection to SAP.

Connection defaults to session 0.

To connect to other sessions of SAP send session number as Argument:

```
# Session 0
session = saptools.SAPConnect()

# Session 1
session = saptools.SAPConnect(1)
```