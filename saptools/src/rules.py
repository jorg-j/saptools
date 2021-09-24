"""
Rules for conversion.
"""
import os

######################### VBS Converter Rules ##########################


def vbsConverter(SAPVB):
    """convert SAP VBS to Python.
    Args: SAPVB (String, NonOptional)
    Returns: SAPVB (String, NonOptional)

    >>> vbsConverter('session.findById("wnd[0]").sendVKey 0')
    'session.findById("wnd[0]").sendVKey (0)'

    >>> vbsConverter('click.press')
    'click.press()'

    >>> vbsConverter('click.setFocus')
    'click.setFocus()'

    """
    needsParenthesis = []
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    import_file = os.path.join(parentdir, "config/parenthesis.txt")

    with open(import_file, "r") as parenthFile:
        filecontents = parenthFile.readlines()

        for line in filecontents:
            current_place = line.replace("\n", "")
            needsParenthesis.append(current_place)

    for action in needsParenthesis:
        if SAPVB.endswith(action):
            return SAPVB + "()"

    if "sendVKey" in SAPVB:
        SplitLine = SAPVB.split(" ")
        SplitLine[1] = "(" + SplitLine[1] + ")"
        return " ".join(SplitLine)
    else:
        return SAPVB


# -----------------------------------------------------------------------
