from compiler.outlier import *

class SymbolTable:
    __func = 'functions'
    __sym = 'symbols'
    __local = 'local'

    __table = {
        __func: {},__sym: {},__local: []
    }

    def __is_local(self):
        return len(self.__table[self.__local]) > 0

    def get_sym(self, sym):
        if self.__is_local():
            for tab in reversed(self.__table[self.__local]):
                if sym in tab:
                    return tab[sym]

        if sym in self.__table[self.__sym]:
            return self.__table[self.__sym][sym]

        raise SymbolNotFound("Undefined variable '%s'" % sym)
