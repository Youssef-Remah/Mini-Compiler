'''
This file contains regular expression patterns corresponding to specific tokens in the MIPS Assembly Language.

Each pattern is designed to match and identify particular tokens during lexical analysis.

'''

import re

decimal_regex = re.compile(pattern = r'^-?\d+$')

comma_regex = re.compile(pattern = r'^,+$')

left_paren_regex = re.compile(pattern = r'^\(+$')

right_paren_regex = re.compile(pattern = r'^\)+$')

# 1) String starts with a letter from a-z or A-Z, and all other chars are a-z, A-Z, 0-9, or _
identifier_regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]*$')

# 2) String starts with a dot and the other chars are a-z or A-Z
dot_identifier_regex = re.compile(r'^\.[a-zA-Z]+$')

# 3) String starts with $ dollar sign, the second char is a letter from a-z or A-Z,
# and the third char is a number 0-9
register_regex = re.compile(r'^\$[a-zA-Z][0-9]$')

# if comma_regex.match(''):
#     print('match found')
# else:
#     print('match not found')

