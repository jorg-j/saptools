"""
Rules for conversion.
"""


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

    with open("config/parenthesis.txt", "r") as parenthFile:
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
