import re


decimal_regex = re.compile(pattern = r'^-?\d+$')


comma_regex = re.compile(pattern = r'^,+$')


left_paren_regex = re.compile(pattern = r'^\(+$')


right_paren_regex = re.compile(pattern = r'^\)+$')


identifier_regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]*$')


dot_identifier_regex = re.compile(r'^\.[a-zA-Z]+$')


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

            return ('Lexem=' + lexem, 'Token=' + lexem)
        
        else:
            
            return ('Lexem=' + lexem, 'Token=identifier')
    
    # 2- check dot identifier (i.e. Directive)
    elif dot_identifier_regex.match(lexem):
        
        return ('Lexem=' + lexem, 'Token=dot-identifier')

    # 3- check register
    elif register_regex.match(lexem):

        return ('Lexem=' + lexem, 'Token=register')
    
    # 4- check decimal numbers
    elif decimal_regex.match(lexem):

        return ('Lexem=' + lexem, 'Token=decimal')

    # 5- check left parentheses
    elif left_paren_regex.match(lexem):

        return ('Lexem=' + lexem, 'Token=left-paren')
    
    # 6- check right parentheses
    elif right_paren_regex.match(lexem):

        return ('Lexem=' + lexem, 'Token=right-paren')

    # 7- check comma
    else:
        return ('Lexem=' + lexem, 'Token=comma')


def create_lexem_token_table(lexems_list):

    size = len(lexems_list)

    symbol_table = []
    
    for i in range(size):

        # check if current lexem is last lexem
        if (i+1) == (size):

            symbol_table.append( tokenizer(lexems_list[i], '') )

        else:

            symbol_table.append( tokenizer(lexems_list[i], lexems_list[i + 1]) )

    return symbol_table


def create_symbol_table(lexems_list):

    symbol_table = []

    for (lexem, token) in lexems_list:

        if token == 'Token=identifier':

            symbol_table.append( ( 'Name={}'.format(lexem[6:]), 'Type=memory address' ) )
    
    return symbol_table



lexems_list = create_lexem_token_table(lexems_list)

symbol_table = create_symbol_table(lexems_list)

print('\n\n********************* Lexems and Tokens Table *********************\n\n')

print(lexems_list)

print('\n\n********************* Symbol Table *********************\n\n')

print(symbol_table, end='\n\n')