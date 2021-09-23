#!/usr/bin/python3
"""
Useage: Global Module
Author: jorg-j
https://github.com/jorg-j/
Date: 2021-04-02
Convert SAP VBS code to py format
"""

from src.documentHandling import writer, DocumentSelect, ReadData
from src.rules import vbsConverter
from src.argHandling import *

################################# Main #################################


def getDocument():
    data = args.f
    outfile = args.o

    if not data:
        data = DocumentSelect()
    data = ReadData(data)
    if not outfile:
        outfile = "outfile.py"
    if outfile.endswith(".py") == False:
        outfile += ".py"

    return data, outfile


def main():
    # Get document to process
    data, outfile = getDocument()
    if not data:
        raise SystemError

    # Write SAP Connection to file as new.
    writer(
        line="import saptools\n\nsession = saptools.SAPConnect()\n\ntry:",
        Mode="w",
        OutName=outfile,
    )

    # Write each line to file using the saptools.vbsconverter
    for line in data:
        if "session.findById" in line:
            writer(line="    " + vbsConverter(SAPVB=line), OutName=outfile)

    # Write closing statements to document.
    writer(line="except:", OutName=outfile)
    writer(line="    print(sys.exc_info()[0])", OutName=outfile)


if __name__ == "__main__":
    main()
