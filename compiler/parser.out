Created by PLY version 3.11 (http://www.dabeaz.com/ply)

Unused terminals:

    FUNCTION
    KEYWORD
    NEWLINE
    QUESTION_MARK
    RETURN

Grammar

Rule 0     S' -> statement_list
Rule 1     statement_list -> statement
Rule 2     statement_list -> statement_list statement
Rule 3     statement -> identifier
Rule 4     statement -> expression
Rule 5     statement -> if_statement
Rule 6     identifier -> IDENTIFIER
Rule 7     statement -> EXIT STMT_END
Rule 8     primitive -> NUM_INT
Rule 9     primitive -> NUM_FLOAT
Rule 10    primitive -> STRING
Rule 11    primitive -> boolean
Rule 12    expression -> expression PLUS expression
Rule 13    expression -> expression MINUS expression
Rule 14    expression -> expression MUL expression
Rule 15    expression -> expression DIV expression
Rule 16    expression -> expression EXP expression
Rule 17    expression -> expression MOD expression
Rule 18    expression -> expression BIT_AND expression
Rule 19    expression -> expression BIT_OR expression
Rule 20    expression -> expression BIT_XOR expression
Rule 21    expression -> expression LSHIFT expression
Rule 22    expression -> expression RSHIFT expression
Rule 23    boolean -> expression EQ expression
Rule 24    boolean -> expression NEQ expression
Rule 25    boolean -> expression GT expression
Rule 26    boolean -> expression GTE expression
Rule 27    boolean -> expression LT expression
Rule 28    boolean -> expression LTE expression
Rule 29    boolean -> expression AND expression
Rule 30    boolean -> expression OR expression
Rule 31    expression -> MINUS expression
Rule 32    expression -> PLUS expression
Rule 33    expression -> BIT_NEG expression
Rule 34    expression -> NOT expression
Rule 35    expression -> LPAREN expression RPAREN
Rule 36    boolean -> TRUE
Rule 37    boolean -> FALSE
Rule 38    assignable -> primitive
Rule 39    assignable -> expression
Rule 40    arguments -> arguments COMMA expression
Rule 41    arguments -> expression
Rule 42    arguments -> <empty>
Rule 43    statement -> identifier LSQBRACK expression RSQBRACK EQUALS expression STMT_END
Rule 44    expression -> identifier EQUALS assignable STMT_END
Rule 45    if_statement -> IF expression LBRACK statement_list RBRACK
Rule 46    if_statement -> IF expression LBRACK statement_list RBRACK ELSE LBRACK statement_list RBRACK
Rule 47    if_statement -> IF expression LBRACK statement_list RBRACK ELSE if_statement
Rule 48    expression -> expression IN expression
Rule 49    expression -> expression NOT IN expression
Rule 50    statement -> PRINT arguments STMT_END
Rule 51    expression -> identifier DOUBLE_PLUS
Rule 52    expression -> identifier DOUBLE_MINUS
Rule 53    expression -> primitive
Rule 54    expression -> STRING
Rule 55    expression -> identifier
Rule 56    statement -> WHILE expression LBRACK statement_list RBRACK
Rule 57    statement -> FOR LBRACK statement_list RBRACK

Terminals, with rules where they appear

AND                  : 29
COMMA                : 40
DIV                  : 15
DOUBLE_MINUS         : 52
DOUBLE_PLUS          : 51
ELSE                 : 46 47
EQ                   : 23
EQUALS               : 43 44
EXIT                 : 7
EXP                  : 16
FALSE                : 37
FOR                  : 57
FUNCTION             : 
GT                   : 25
GTE                  : 26
IDENTIFIER           : 6
IF                   : 45 46 47
IN                   : 48 49
KEYWORD              : 
LBRACK               : 45 46 46 47 56 57
LPAREN               : 35
LSHIFT               : 21
LSQBRACK             : 43
LT                   : 27
LTE                  : 28
MINUS                : 13 31
MOD                  : 17
MUL                  : 14
NEQ                  : 24
NEWLINE              : 
NOT                  : 34 49
NUM_FLOAT            : 9
NUM_INT              : 8
OR                   : 30
PLUS                 : 12 32
PRINT                : 50
QUESTION_MARK        : 
RBRACK               : 45 46 46 47 56 57
RETURN               : 
RPAREN               : 35
RSHIFT               : 22
RSQBRACK             : 43
STMT_END             : 7 43 44 50
STRING               : 10 54
TRUE                 : 36
WHILE                : 56
error                : 

Nonterminals, with rules where they appear

BIT_AND              : 18
BIT_NEG              : 33
BIT_OR               : 19
BIT_XOR              : 20
arguments            : 40 50
assignable           : 44
boolean              : 11
expression           : 4 12 12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20 20 21 21 22 22 23 23 24 24 25 25 26 26 27 27 28 28 29 29 30 30 31 32 33 34 35 39 40 41 43 43 45 46 47 48 48 49 49 56
identifier           : 3 43 44 51 52 55
if_statement         : 5 47
primitive            : 38 53
statement            : 1 2
statement_list       : 2 45 46 46 47 56 57 0
