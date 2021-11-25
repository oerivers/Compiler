import ply.lex as lex
import compiler.exceptions

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

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    t.lexer.linepos = 0
    pass

def t_TRUE(t):
    'true'
    t.value = True
    return t

def t_FALSE(t):
    'false'
    t.value = False
    return t

def t_IDENTIFIER(t):
    r'[\$_a-zA-Z]\w*'

    t.type = reserved.get(t.value, t.type)

    return t

def t_NUM_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"(?:\\"|.)*?"'

    t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")
    return t

def t_error(t):
    raise comp_final.exceptions.UnexpectedCharacter("Unexpected character '%s' at line %d" % (t.value[0], t.lineno))

lexer = lex.lex()
