"""
Standard module for handling arguments
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", help="Filepath for conversion")
parser.add_argument("-o", help="Outputfile")

args = parser.parse_args()
