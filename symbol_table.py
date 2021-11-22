from compiler.outlier import *

class SymbolTable:
    __func = 'functions'
    __sym = 'symbols'
    __local = 'local'

    __table = {
        __func: {},__sym: {},__local: []
    }
