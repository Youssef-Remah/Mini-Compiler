# lexems_list_test = ['lw', '$t0', ',', 'num1', 'lw', '$t1', ',', 'num2', 'add', '$t2', ',', '$t0', ',', '$t1', 'sw', '$t2', ',', 'sum']

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


def read_mips_instructions_file():
    with open('mips_instructions.txt', 'r') as file:
        content = file.read()
    return content

instructions = read_mips_instructions_file()

def split_string_by_whitespace(instructions):
    # Using the split() method to split the string based on white spaces

    words = instructions.split()

    return words


def insert_spaces_around_commas(input_string):
    # Split the string into a list based on commas
    substrings = input_string.split(',')

    # Join the substrings with spaces around commas
    result_string = ' , '.join(substring.strip() for substring in substrings)

    return result_string

instructions = insert_spaces_around_commas(instructions)

lexems_list = split_string_by_whitespace(instructions)

def tokenizer(lexem, nextLexem):

    # 1- check identifier
    if identifier_regex.match(lexem):

        # 1.1- check if reserved word (i.e. next lexem is a register)

        if register_regex.match(nextLexem) or decimal_regex.match(nextLexem):

            return (lexem, lexem)
        
        else:
            
            return (lexem, 'identifier')
    
    # 2- check dot identifier (i.e. Directive)
    elif dot_identifier_regex.match(lexem):
        
        return (lexem, 'dot-identifier')

    # 3- check register
    elif register_regex.match(lexem):

        return (lexem, 'register')
    
    # 4- check decimal numbers
    elif decimal_regex.match(lexem):

        return (lexem, 'decimal')

    # 5- check left parentheses
    elif left_paren_regex.match(lexem):

        return (lexem, 'left-paren')
    
    # 6- check right parentheses
    elif right_paren_regex.match(lexem):

        return (lexem, 'right-paren')

    # 7- check comma
    else:
        return (lexem, 'comma')


def create_symbol_table(lexems_list):

    size = len(lexems_list)

    symbol_table = []
    
    for i in range(size):

        # check if current lexem is last lexem
        if (i+1) == (size):

            symbol_table.append( tokenizer(lexems_list[i], '') )

        else:

            symbol_table.append( tokenizer(lexems_list[i], lexems_list[i + 1]) )

    return symbol_table


print(create_symbol_table(lexems_list))