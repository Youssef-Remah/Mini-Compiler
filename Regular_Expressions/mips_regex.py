'''
This file contains regular expression patterns corresponding to specific tokens in the MIPS Assembly Language.

Each pattern is designed to match and identify particular tokens during lexical analysis.

'''

import re

decimal_regex = re.compile(pattern = r'^-?\d+$')

comma_regex = re.compile(pattern = r'^,+$')

left_paran_regex = re.compile(pattern = r'^\(+$')

right_paran_regex = re.compile(pattern = r'^\)+$')

