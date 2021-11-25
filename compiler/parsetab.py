# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftNOTleftPLUSMINUSleftMULDIVleftEXPMODrightUMINUSrightUPLUSAND BIT_AND BIT_NEG BIT_OR BIT_XOR COMMA DIV DOUBLE_MINUS DOUBLE_PLUS ELSE EQ EQUALS EXIT EXP FALSE FOR FUNCTION GT GTE IDENTIFIER IF IN KEYWORD LBRACK LPAREN LSHIFT LSQBRACK LT LTE MINUS MOD MUL NEQ NEWLINE NOT NUM_FLOAT NUM_INT OR PLUS PRINT QUESTION_MARK RBRACK RETURN RPAREN RSHIFT RSQBRACK STMT_END STRING TRUE WHILE\n    statement_list : statement\n                   | statement_list statement\n    \n    statement : identifier\n              | expression\n              | if_statement\n    \n    identifier : IDENTIFIER\n    \n    statement : EXIT STMT_END\n    \n    primitive : NUM_INT\n              | NUM_FLOAT\n              | STRING\n              | boolean\n    \n    expression : expression PLUS expression %prec PLUS\n            | expression MINUS expression %prec MINUS\n            | expression MUL expression %prec MUL\n            | expression DIV expression %prec DIV\n            | expression EXP expression %prec EXP\n            | expression MOD expression %prec MOD\n\n            | expression BIT_AND expression\n            | expression BIT_OR expression\n            | expression BIT_XOR expression\n            | expression LSHIFT expression\n            | expression RSHIFT expression\n    \n    boolean : expression EQ expression\n            | expression NEQ expression\n            | expression GT expression\n            | expression GTE expression\n            | expression LT expression\n            | expression LTE expression\n            | expression AND expression\n            | expression OR expression\n    \n    expression : MINUS expression %prec UMINUS\n               | PLUS expression %prec UPLUS\n               | BIT_NEG expression\n               | NOT expression\n    \n    expression : LPAREN expression RPAREN\n    \n    boolean : TRUE\n            | FALSE\n    \n    assignable : primitive\n               | expression\n    \n    arguments : arguments COMMA expression\n              | expression\n              |\n    \n    statement : identifier LSQBRACK expression RSQBRACK EQUALS expression STMT_END\n    \n    expression : identifier EQUALS assignable STMT_END\n    \n    if_statement : IF expression LBRACK statement_list RBRACK\n    \n    if_statement : IF expression LBRACK statement_list RBRACK ELSE LBRACK statement_list RBRACK\n    \n    if_statement : IF expression LBRACK statement_list RBRACK ELSE if_statement\n    \n    expression : expression IN expression\n               | expression NOT IN expression\n    \n    statement : PRINT arguments STMT_END\n    \n    expression : identifier DOUBLE_PLUS\n               | identifier DOUBLE_MINUS\n    \n    expression : primitive\n               | STRING\n               | identifier\n    \n    statement : WHILE expression LBRACK statement_list RBRACK\n    \n    statement : FOR LBRACK statement_list RBRACK\n    '
    
_lr_action_items = {'EXIT':([0,1,2,3,4,5,10,16,17,19,20,21,22,23,24,27,28,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,88,90,91,92,93,95,96,98,99,100,102,103,106,107,108,109,110,],[6,6,-1,-3,-4,-5,-6,-53,-10,-8,-9,-11,-36,-37,-2,-51,-52,-7,-55,6,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-50,6,6,-35,6,-44,-49,6,-57,6,-56,-45,-43,6,-47,6,-46,]),'PRINT':([0,1,2,3,4,5,10,16,17,19,20,21,22,23,24,27,28,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,88,90,91,92,93,95,96,98,99,100,102,103,106,107,108,109,110,],[7,7,-1,-3,-4,-5,-6,-53,-10,-8,-9,-11,-36,-37,-2,-51,-52,-7,-55,7,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-50,7,7,-35,7,-44,-49,7,-57,7,-56,-45,-43,7,-47,7,-46,]),'WHILE':([0,1,2,3,4,5,10,16,17,19,20,21,22,23,24,27,28,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,88,90,91,92,93,95,96,98,99,100,102,103,106,107,108,109,110,],[8,8,-1,-3,-4,-5,-6,-53,-10,-8,-9,-11,-36,-37,-2,-51,-52,-7,-55,8,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-50,8,8,-35,8,-44,-49,8,-57,8,-56,-45,-43,8,-47,8,-46,]),'FOR':([0,1,2,3,4,5,10,16,17,19,20,21,22,23,24,27,28,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,88,90,91,92,93,95,96,98,99,100,102,103,106,107,108,109,110,],[9,9,-1,-3,-4,-5,-6,-53,-10,-8,-9,-11,-36,-37,-2,-51,-52,-7,-55,9,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-50,9,9,-35,9,-44,-49,9,-57,9,-56,-45,-43,9,-47,9,-46,]),'IDENTIFIER':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,98,99,100,101,102,103,106,107,108,109,110,],[10,10,-1,-3,-4,-5,10,10,-6,10,10,10,10,10,-53,-10,10,-8,-9,-11,-36,-37,-2,10,10,-51,-52,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-7,-55,10,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,10,-23,-24,-25,-26,-27,-28,-29,-30,-50,10,10,10,-35,10,-44,-49,10,-57,10,10,-56,-45,-43,10,-47,10,-46,]),'MINUS':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,99,100,101,102,103,104,106,107,108,109,110,],[12,12,-1,-3,30,-5,12,12,-6,12,12,12,12,12,-53,-10,12,-8,-9,-11,-36,-37,-2,12,12,-51,-52,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-7,30,-55,30,12,-32,-31,30,30,30,30,30,-53,30,-10,-12,-13,-14,-15,-16,-17,30,30,30,30,30,30,12,30,30,30,30,30,30,30,30,-50,12,12,12,-35,12,-44,30,30,12,-57,12,12,-56,-45,30,-43,12,-47,12,-46,]),'PLUS':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,99,100,101,102,103,104,106,107,108,109,110,],[11,11,-1,-3,29,-5,11,11,-6,11,11,11,11,11,-53,-10,11,-8,-9,-11,-36,-37,-2,11,11,-51,-52,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-7,29,-55,29,11,-32,-31,29,29,29,29,29,-53,29,-10,-12,-13,-14,-15,-16,-17,29,29,29,29,29,29,11,29,29,29,29,29,29,29,29,-50,11,11,11,-35,11,-44,29,29,11,-57,11,11,-56,-45,29,-43,11,-47,11,-46,]),'BIT_NEG':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,98,99,100,101,102,103,106,107,108,109,110,],[13,13,-1,-3,-4,-5,13,13,-6,13,13,13,13,13,-53,-10,13,-8,-9,-11,-36,-37,-2,13,13,-51,-52,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-7,-55,13,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,13,-23,-24,-25,-26,-27,-28,-29,-30,-50,13,13,13,-35,13,-44,-49,13,-57,13,13,-56,-45,-43,13,-47,13,-46,]),'NOT':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,99,100,101,102,103,104,106,107,108,109,110,],[14,14,-1,-3,41,-5,14,14,-6,14,14,14,14,14,-53,-10,14,-8,-9,-11,-36,-37,-2,14,14,-51,-52,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-7,41,-55,41,14,-32,-31,41,-34,41,41,41,-53,41,-10,-12,-13,-14,-15,-16,-17,41,41,41,41,41,41,14,41,41,41,41,41,41,41,41,-50,14,14,14,-35,14,-44,41,41,14,-57,14,14,-56,-45,41,-43,14,-47,14,-46,]),'LPAREN':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,98,99,100,101,102,103,106,107,108,109,110,],[15,15,-1,-3,-4,-5,15,15,-6,15,15,15,15,15,-53,-10,15,-8,-9,-11,-36,-37,-2,15,15,-51,-52,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-7,-55,15,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,15,-23,-24,-25,-26,-27,-28,-29,-30,-50,15,15,15,-35,15,-44,-49,15,-57,15,15,-56,-45,-43,15,-47,15,-46,]),'STRING':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,98,99,100,101,102,103,106,107,108,109,110,],[17,17,-1,-3,-4,-5,17,17,-6,17,17,17,17,17,-53,-10,17,-8,-9,-11,-36,-37,-2,17,66,-51,-52,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-7,-55,17,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,17,-23,-24,-25,-26,-27,-28,-29,-30,-50,17,17,17,-35,17,-44,-49,17,-57,17,17,-56,-45,-43,17,-47,17,-46,]),'IF':([0,1,2,3,4,5,10,16,17,19,20,21,22,23,24,27,28,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,88,90,91,92,93,95,96,98,99,100,102,103,105,106,107,108,109,110,],[18,18,-1,-3,-4,-5,-6,-53,-10,-8,-9,-11,-36,-37,-2,-51,-52,-7,-55,18,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-50,18,18,-35,18,-44,-49,18,-57,18,-56,-45,18,-43,18,-47,18,-46,]),'NUM_INT':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,98,99,100,101,102,103,106,107,108,109,110,],[19,19,-1,-3,-4,-5,19,19,-6,19,19,19,19,19,-53,-10,19,-8,-9,-11,-36,-37,-2,19,19,-51,-52,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-7,-55,19,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,19,-23,-24,-25,-26,-27,-28,-29,-30,-50,19,19,19,-35,19,-44,-49,19,-57,19,19,-56,-45,-43,19,-47,19,-46,]),'NUM_FLOAT':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,98,99,100,101,102,103,106,107,108,109,110,],[20,20,-1,-3,-4,-5,20,20,-6,20,20,20,20,20,-53,-10,20,-8,-9,-11,-36,-37,-2,20,20,-51,-52,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-7,-55,20,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,20,-23,-24,-25,-26,-27,-28,-29,-30,-50,20,20,20,-35,20,-44,-49,20,-57,20,20,-56,-45,-43,20,-47,20,-46,]),'TRUE':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,98,99,100,101,102,103,106,107,108,109,110,],[22,22,-1,-3,-4,-5,22,22,-6,22,22,22,22,22,-53,-10,22,-8,-9,-11,-36,-37,-2,22,22,-51,-52,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-7,-55,22,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,22,-23,-24,-25,-26,-27,-28,-29,-30,-50,22,22,22,-35,22,-44,-49,22,-57,22,22,-56,-45,-43,22,-47,22,-46,]),'FALSE':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,53,55,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,98,99,100,101,102,103,106,107,108,109,110,],[23,23,-1,-3,-4,-5,23,23,-6,23,23,23,23,23,-53,-10,23,-8,-9,-11,-36,-37,-2,23,23,-51,-52,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-7,-55,23,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,23,-23,-24,-25,-26,-27,-28,-29,-30,-50,23,23,23,-35,23,-44,-49,23,-57,23,23,-56,-45,-43,23,-47,23,-46,]),'$end':([1,2,3,4,5,10,16,17,19,20,21,22,23,24,27,28,50,53,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,88,92,95,96,99,102,103,106,108,110,],[0,-1,-3,-4,-5,-6,-53,-10,-8,-9,-11,-36,-37,-2,-51,-52,-7,-55,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-50,-35,-44,-49,-57,-56,-45,-43,-47,-46,]),'RBRACK':([2,3,4,5,10,16,17,19,20,21,22,23,24,27,28,50,53,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,88,91,92,95,96,98,99,100,102,103,106,108,109,110,],[-1,-3,-4,-5,-6,-53,-10,-8,-9,-11,-36,-37,-2,-51,-52,-7,-55,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-50,99,-35,-44,-49,102,-57,103,-56,-45,-43,-47,110,-46,]),'LSQBRACK':([3,10,],[25,-6,]),'EQUALS':([3,10,53,94,],[26,-6,26,101,]),'DOUBLE_PLUS':([3,10,53,],[27,-6,27,]),'DOUBLE_MINUS':([3,10,53,],[28,-6,28,]),'MUL':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,31,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,31,-55,31,-32,-31,31,31,31,31,31,-53,31,-10,31,31,-14,-15,-16,-17,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-35,-44,31,31,31,]),'DIV':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,32,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,32,-55,32,-32,-31,32,32,32,32,32,-53,32,-10,32,32,-14,-15,-16,-17,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-35,-44,32,32,32,]),'EXP':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,33,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,33,-55,33,-32,-31,33,33,33,33,33,-53,33,-10,33,33,33,33,-16,-17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-35,-44,33,33,33,]),'MOD':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,34,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,34,-55,34,-32,-31,34,34,34,34,34,-53,34,-10,34,34,34,34,-16,-17,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-35,-44,34,34,34,]),'BIT_AND':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,35,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,35,-55,35,-32,-31,35,-34,35,35,35,-53,35,-10,-12,-13,-14,-15,-16,-17,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-35,-44,35,35,35,]),'BIT_OR':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,36,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,36,-55,36,-32,-31,36,-34,36,36,36,-53,36,-10,-12,-13,-14,-15,-16,-17,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-35,-44,36,36,36,]),'BIT_XOR':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,37,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,37,-55,37,-32,-31,37,-34,37,37,37,-53,37,-10,-12,-13,-14,-15,-16,-17,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-35,-44,37,37,37,]),'LSHIFT':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,38,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,38,-55,38,-32,-31,38,-34,38,38,38,-53,38,-10,-12,-13,-14,-15,-16,-17,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-35,-44,38,38,38,]),'RSHIFT':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,39,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,39,-55,39,-32,-31,39,-34,39,39,39,-53,39,-10,-12,-13,-14,-15,-16,-17,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-35,-44,39,39,39,]),'IN':([3,4,10,16,17,19,20,21,22,23,27,28,41,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,40,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,79,40,-55,40,-32,-31,40,-34,40,40,40,-53,40,-10,-12,-13,-14,-15,-16,-17,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-35,-44,40,40,40,]),'EQ':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,42,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,42,-55,42,-32,-31,42,-34,42,42,42,-53,42,-10,-12,-13,-14,-15,-16,-17,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-35,-44,42,42,42,]),'NEQ':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,43,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,43,-55,43,-32,-31,43,-34,43,43,43,-53,43,-10,-12,-13,-14,-15,-16,-17,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-35,-44,43,43,43,]),'GT':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,44,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,44,-55,44,-32,-31,44,-34,44,44,44,-53,44,-10,-12,-13,-14,-15,-16,-17,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-35,-44,44,44,44,]),'GTE':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,45,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,45,-55,45,-32,-31,45,-34,45,45,45,-53,45,-10,-12,-13,-14,-15,-16,-17,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-35,-44,45,45,45,]),'LT':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,46,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,46,-55,46,-32,-31,46,-34,46,46,46,-53,46,-10,-12,-13,-14,-15,-16,-17,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-35,-44,46,46,46,]),'LTE':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,47,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,47,-55,47,-32,-31,47,-34,47,47,47,-53,47,-10,-12,-13,-14,-15,-16,-17,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-35,-44,47,47,47,]),'AND':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,48,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,48,-55,48,-32,-31,48,-34,48,48,48,-53,48,-10,-12,-13,-14,-15,-16,-17,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-35,-44,48,48,48,]),'OR':([3,4,10,16,17,19,20,21,22,23,27,28,52,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[-55,49,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,49,-55,49,-32,-31,49,-34,49,49,49,-53,49,-10,-12,-13,-14,-15,-16,-17,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-35,-44,49,49,49,]),'STMT_END':([6,7,10,16,17,19,20,21,22,23,27,28,51,52,53,56,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,104,],[50,-42,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,88,-41,-55,-32,-31,-33,-34,95,-38,-39,-10,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-35,-44,-49,-40,106,]),'COMMA':([7,10,16,17,19,20,21,22,23,27,28,51,52,53,56,57,58,59,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,97,],[-42,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,89,-41,-55,-32,-31,-33,-34,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-35,-44,-49,-40,]),'LBRACK':([9,10,16,17,19,20,21,22,23,27,28,53,54,56,57,58,59,61,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,105,],[55,-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,-55,90,-32,-31,-33,-34,93,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-35,-44,-49,107,]),'RPAREN':([10,16,17,19,20,21,22,23,27,28,53,56,57,58,59,60,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,],[-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,-55,-32,-31,-33,-34,92,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-35,-44,-49,]),'RSQBRACK':([10,16,17,19,20,21,22,23,27,28,53,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,92,95,96,],[-6,-53,-10,-8,-9,-11,-36,-37,-51,-52,-55,-32,-31,-33,-34,94,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-48,-23,-24,-25,-26,-27,-28,-29,-30,-35,-44,-49,]),'ELSE':([103,],[105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,55,90,93,107,],[1,91,98,100,109,]),'statement':([0,1,55,90,91,93,98,100,107,109,],[2,24,2,2,24,2,24,24,2,24,]),'identifier':([0,1,7,8,11,12,13,14,15,18,25,26,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,55,79,89,90,91,93,98,100,101,107,109,],[3,3,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,3,53,53,3,3,3,3,3,53,3,3,]),'expression':([0,1,7,8,11,12,13,14,15,18,25,26,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,55,79,89,90,91,93,98,100,101,107,109,],[4,4,52,54,56,57,58,59,60,61,62,65,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,4,96,97,4,4,4,4,4,104,4,4,]),'if_statement':([0,1,55,90,91,93,98,100,105,107,109,],[5,5,5,5,5,5,5,5,108,5,5,]),'primitive':([0,1,7,8,11,12,13,14,15,18,25,26,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,55,79,89,90,91,93,98,100,101,107,109,],[16,16,16,16,16,16,16,16,16,16,16,64,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'boolean':([0,1,7,8,11,12,13,14,15,18,25,26,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,55,79,89,90,91,93,98,100,101,107,109,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'arguments':([7,],[51,]),'assignable':([26,],[63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement_list","S'",1,None,None,None),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',20),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',21),
  ('statement -> identifier','statement',1,'p_statement','parser.py',32),
  ('statement -> expression','statement',1,'p_statement','parser.py',33),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',34),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier','parser.py',41),
  ('statement -> EXIT STMT_END','statement',2,'p_exit_stmt','parser.py',48),
  ('primitive -> NUM_INT','primitive',1,'p_primitive','parser.py',56),
  ('primitive -> NUM_FLOAT','primitive',1,'p_primitive','parser.py',57),
  ('primitive -> STRING','primitive',1,'p_primitive','parser.py',58),
  ('primitive -> boolean','primitive',1,'p_primitive','parser.py',59),
  ('expression -> expression PLUS expression','expression',3,'p_binary_op','parser.py',69),
  ('expression -> expression MINUS expression','expression',3,'p_binary_op','parser.py',70),
  ('expression -> expression MUL expression','expression',3,'p_binary_op','parser.py',71),
  ('expression -> expression DIV expression','expression',3,'p_binary_op','parser.py',72),
  ('expression -> expression EXP expression','expression',3,'p_binary_op','parser.py',73),
  ('expression -> expression MOD expression','expression',3,'p_binary_op','parser.py',74),
  ('expression -> expression BIT_AND expression','expression',3,'p_binary_op','parser.py',76),
  ('expression -> expression BIT_OR expression','expression',3,'p_binary_op','parser.py',77),
  ('expression -> expression BIT_XOR expression','expression',3,'p_binary_op','parser.py',78),
  ('expression -> expression LSHIFT expression','expression',3,'p_binary_op','parser.py',79),
  ('expression -> expression RSHIFT expression','expression',3,'p_binary_op','parser.py',80),
  ('boolean -> expression EQ expression','boolean',3,'p_boolean_operators','parser.py',87),
  ('boolean -> expression NEQ expression','boolean',3,'p_boolean_operators','parser.py',88),
  ('boolean -> expression GT expression','boolean',3,'p_boolean_operators','parser.py',89),
  ('boolean -> expression GTE expression','boolean',3,'p_boolean_operators','parser.py',90),
  ('boolean -> expression LT expression','boolean',3,'p_boolean_operators','parser.py',91),
  ('boolean -> expression LTE expression','boolean',3,'p_boolean_operators','parser.py',92),
  ('boolean -> expression AND expression','boolean',3,'p_boolean_operators','parser.py',93),
  ('boolean -> expression OR expression','boolean',3,'p_boolean_operators','parser.py',94),
  ('expression -> MINUS expression','expression',2,'p_unary_operation','parser.py',102),
  ('expression -> PLUS expression','expression',2,'p_unary_operation','parser.py',103),
  ('expression -> BIT_NEG expression','expression',2,'p_unary_operation','parser.py',104),
  ('expression -> NOT expression','expression',2,'p_unary_operation','parser.py',105),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_paren','parser.py',113),
  ('boolean -> TRUE','boolean',1,'p_boolean','parser.py',121),
  ('boolean -> FALSE','boolean',1,'p_boolean','parser.py',122),
  ('assignable -> primitive','assignable',1,'p_assignable','parser.py',130),
  ('assignable -> expression','assignable',1,'p_assignable','parser.py',131),
  ('arguments -> arguments COMMA expression','arguments',3,'p_comma_separated_expr','parser.py',139),
  ('arguments -> expression','arguments',1,'p_comma_separated_expr','parser.py',140),
  ('arguments -> <empty>','arguments',0,'p_comma_separated_expr','parser.py',141),
  ('statement -> identifier LSQBRACK expression RSQBRACK EQUALS expression STMT_END','statement',7,'p_array_access_assign','parser.py',154),
  ('expression -> identifier EQUALS assignable STMT_END','expression',4,'p_assign','parser.py',162),
  ('if_statement -> IF expression LBRACK statement_list RBRACK','if_statement',5,'p_ifstatement','parser.py',170),
  ('if_statement -> IF expression LBRACK statement_list RBRACK ELSE LBRACK statement_list RBRACK','if_statement',9,'p_ifstatement_else','parser.py',178),
  ('if_statement -> IF expression LBRACK statement_list RBRACK ELSE if_statement','if_statement',7,'p_ifstatement_else_if','parser.py',185),
  ('expression -> expression IN expression','expression',3,'p_in_expression','parser.py',193),
  ('expression -> expression NOT IN expression','expression',4,'p_in_expression','parser.py',194),
  ('statement -> PRINT arguments STMT_END','statement',3,'p_print_statement','parser.py',205),
  ('expression -> identifier DOUBLE_PLUS','expression',2,'p_increment_decrement_identifiers','parser.py',213),
  ('expression -> identifier DOUBLE_MINUS','expression',2,'p_increment_decrement_identifiers','parser.py',214),
  ('expression -> primitive','expression',1,'p_expression','parser.py',225),
  ('expression -> STRING','expression',1,'p_expression','parser.py',226),
  ('expression -> identifier','expression',1,'p_expression','parser.py',227),
  ('statement -> WHILE expression LBRACK statement_list RBRACK','statement',5,'p_while_loop','parser.py',234),
  ('statement -> FOR LBRACK statement_list RBRACK','statement',4,'p_for_loop_infinite','parser.py',242),
]
