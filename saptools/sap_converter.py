#!/usr/bin/python3
"""
Useage: Global Module
Author: jorg-j
https://github.com/jorg-j/
Date: 2021-09-23
Convert SAP VBS code to py format
"""

from src.argHandling import *
from src.document_handling import document_select, read_data, writer
from src.rules import vbsConverter

################################# Main #################################


def cleanup_filename(out_file):

    if out_file.endswith(".py") == False:
        out_file += ".py"

    return out_file


def convert_file(Document=None, out_file="outfile.py"):
    if not Document:
        Document = document_select()

    out_file = cleanup_filename()
    data = read_data(Document)
    if not data:
        raise SystemError

    # Write SAP Connection to file as new.
    writer(
        line="import saptools\n\nsession = saptools.SAPConnect()\n\ntry:",
        Mode="w",
        OutName=out_file,
    )

    # Write each line to file using the saptools.vbsconverter
    for line in data:
        if "session.findById" in line:
            writer(line="    " + vbsConverter(SAPVB=line), OutName=out_file)

    # Write closing statements to document.
    writer(line="except:", OutName=out_file)
    writer(line="    print(sys.exc_info()[0])", OutName=out_file)