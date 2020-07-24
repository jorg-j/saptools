'''
Useage: Global Module
Author: jorg-j
https://github.com/jorg-j/
Date: 24-07-2020

Dependencies:
    tkinter - for file dialog

'''

import doctest
from tkinter import *
from tkinter import filedialog

'''
Convert SAP VBS code to py format
'''

#-----------------------------------------------------------------------

######################### Write/Append to File #########################

def writer(line, Mode='a+', OutName='outfile.py'):
    ''' 
    Handles the writing to file of translated information.
    Args: line(str, nonoptional) Write data
    Mode(str, optional) file mode, default append
    OutName(str, optional) filename to save as
    '''
    with open(OutName, Mode)as f:
        f.write(line)
        f.write('\n')

#-----------------------------------------------------------------------

########################## Document Selector ###########################

def DocumentSelect():
    root = Tk()
    root.filename =  filedialog.askopenfilename()
    filepath = root.filename
    root.destroy()
    data = ReadData(filepath=filepath)
    return data

#-----------------------------------------------------------------------

############################## Read File ##############################

def ReadData(filepath):
    with open(filepath, 'r')as f:
        '''read in data'''
        data = f.read()
    data = data.split('\n')
    return data


#-----------------------------------------------------------------------

######################### VBS Converter Rules ##########################

def vbsConverter(SAPVB):
    '''convert SAP VBS to Python.
    Args: SAPVB (String, NonOptional)
    Returns: SAPVB (String, NonOptional)

    >>> vbsConverter('session.findById("wnd[0]").sendVKey 0')
    'session.findById("wnd[0]").sendVKey (0)'

    >>> vbsConverter('click.press')
    'click.press()'

    >>> vbsConverter('click.setFocus')
    'click.setFocus()'

    '''
    needsBrackets : list = [
        '.press', '.maximize',
        '.doubleClickCurrentCell',
        '.select', '.setFocus'
    ]

    for action in needsBrackets:
        if SAPVB.endswith(action):
            return SAPVB + '()'

    if 'sendVKey' in SAPVB:
        SplitLine = SAPVB.split(' ')
        SplitLine[1] = '(' + SplitLine[1] + ')'
        return " ".join(SplitLine)

    else:
        return SAPVB

#-----------------------------------------------------------------------

################################# Main #################################

def main():
    data = DocumentSelect()

    # Write SAP Connection to file as new.
    writer(line='session = saptools.SAPConnect()\n\ntry:', Mode='w')

    # Write each line to file using the saptools.vbsconverter
    for line in data:
        if 'session.findById' in line:
            writer(line="    " + saptools.vbsConverter(SAPVB=line))

    # Write closing statements to document.
    writer(line='except:')
    writer(line='    print(sys.exc_info()[0])')


main()

#-----------------------------------------------------------------------

################################# Tests ################################

def test1():
    needsBrackets = [
        '.press', '.maximize',
        '.doubleClickCurrentCell',
        '.select', '.setFocus'
    ]
    for item in needsBrackets:
        result = vbsConverter(f'check{item}')
        assert result == f'check{item}()'

def test2():
    assert vbsConverter('session.findById("wnd[0]").sendVKey 0') == 'session.findById("wnd[0]").sendVKey (0)'


# doctest.testmod()