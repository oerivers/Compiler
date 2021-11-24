import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'while': 'WHILE',
    'exit': 'EXIT',
    'fn': 'FUNCTION',
    'ret': 'RETURN',
    'print': 'PRINT',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
}

tokens = [
    'KEYWORD','STMT_END','EQUALS','IDENTIFIER','NUM_INT','NUM_FLOAT','LPAREN','RPAREN','LBRACK','RBRACK','COMMA','STRING','NEWLINE','LSQBRACK','RSQBRACK','QUESTION_MARK',

    'PLUS','EXP','MINUS','MUL','DIV','MOD','LSHIFT','RSHIFT','BIT_AND','BIT_OR','BIT_XOR','BIT_NEG',

    'DOUBLE_PLUS','DOUBLE_MINUS',

    'TRUE','FALSE',

    'EQ','NEQ','GT','GTE','LT','LTE',
         ] + list(reserved.values())

t_COMMA = ','
t_PLUS = r'\+'
t_EXP = r'\^'
t_MINUS = '-'
t_MUL = r'\*'
t_DIV = r'/'
t_STMT_END = ';'
t_EQUALS = '='
t_ignore_WS = r'\s+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = '{'
t_RBRACK = '}'
t_EQ = '=='
t_NEQ = '!='
t_GT = '>'
t_GTE = '>='
t_LT = '<'
t_LTE = '<='
