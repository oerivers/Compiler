import ply.yacc as yacc

disable_warnings = False

precedence = (
    ('left', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('left', 'EXP', 'MOD'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS'),
)


def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    if len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
    else:
        p[1].children.append(p[2])
        p[0] = p[1]


def p_statement(p):
    '''
    statement : identifier
              | expression
              | if_statement
    '''
    p[0] = p[1]


def p_identifier(p):
    '''
    identifier : IDENTIFIER
    '''
    p[0] = ast.Identifier(p[1])


def p_exit_stmt(p):
    '''
    statement : EXIT STMT_END
    '''
    p[0] = ast.ExitStatement()



def p_primitive(p):
    '''
    primitive : NUM_INT
              | NUM_FLOAT
              | STRING
              | boolean
    '''
    if isinstance(p[1], ast.BaseExpression):
        p[0] = p[1]
    else:
        p[0] = ast.Primitive(p[1])

def p_binary_op(p):
    '''
    expression : expression PLUS expression %prec PLUS
            | expression MINUS expression %prec MINUS
            | expression MUL expression %prec MUL
            | expression DIV expression %prec DIV
            | expression EXP expression %prec EXP
            | expression MOD expression %prec MOD
            | expression BIT_AND expression
            | expression BIT_OR expression
            | expression BIT_XOR expression
            | expression LSHIFT expression
            | expression RSHIFT expression
    '''
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])


def p_boolean_operators(p):
    '''
    boolean : expression EQ expression
            | expression NEQ expression
            | expression GT expression
            | expression GTE expression
            | expression LT expression
            | expression LTE expression
            | expression AND expression
            | expression OR expression
    '''
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])



def p_unary_operation(p):
    '''
    expression : MINUS expression %prec UMINUS
               | PLUS expression %prec UPLUS
               | BIT_NEG expression
               | NOT expression
    '''
    p[0] = ast.UnaryOperation(p[1], p[2])



def p_paren(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2] if isinstance(p[2], ast.BaseExpression) else ast.Primitive(p[2])



def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''
    p[0] = ast.Primitive(p[1])


def p_assignable(p):
    '''
    assignable : primitive
               | expression
    '''
    p[0] = p[1]



def p_comma_separated_expr(p):
    '''
    arguments : arguments COMMA expression
              | expression
              |
    '''
    if len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
    elif len(p) == 1:
        p[0] = ast.InstructionList()
    else:
        p[1].children.append(p[3])
        p[0] = p[1]


def p_array_access_assign(p):
    '''
    statement : identifier LSQBRACK expression RSQBRACK EQUALS expression STMT_END
    '''
    p[0] = ast.ArrayAssign(p[1], p[3], p[6])



def p_assign(p):
    '''
    expression : identifier EQUALS assignable STMT_END
    '''
    p[0] = ast.Assignment(p[1], p[3])



def p_ifstatement(p):
    '''
    if_statement : IF expression LBRACK statement_list RBRACK
    '''
    p[0] = ast.If(p[2], p[4])



def p_ifstatement_else(p):
    '''
    if_statement : IF expression LBRACK statement_list RBRACK ELSE LBRACK statement_list RBRACK
    '''
    p[0] = ast.If(p[2], p[4], p[8])


def p_ifstatement_else_if(p):
    '''
    if_statement : IF expression LBRACK statement_list RBRACK ELSE if_statement
    '''
    p[0] = ast.If(p[2], p[4], p[7])



def p_in_expression(p):
    '''
    expression : expression IN expression
               | expression NOT IN expression
    '''
    if len(p) == 4:
        p[0] = ast.InExpression(p[1], p[3])
    else:
        p[0] = ast.InExpression(p[1], p[4], True)



def p_print_statement(p):
    '''
    statement : PRINT arguments STMT_END
    '''
    p[0] = ast.PrintStatement(p[2])



def p_increment_decrement_identifiers(p):
    '''
    expression : identifier DOUBLE_PLUS
               | identifier DOUBLE_MINUS
    '''
    if p[2] == '++':
        p[0] = ast.BinaryOperation(p[1], ast.Primitive(1), '+')
    else:
        p[0] = ast.BinaryOperation(p[1], ast.Primitive(1), '-')
