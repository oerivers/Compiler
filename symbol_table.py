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

        raise SymbolNotFound("Variable is not defined '%s'" % sym)
  
    def set_sym(self, sym, val):
        if self.__is_local():
            self.get_local_table()[sym] = val
        else:
            self.__table[self.__sym][sym] = val

    def get_func(self, name):
        if name in self.__table[self.__func]:
            return self.__table[self.__func][name]
       
        raise SymbolNotFound("Function is undefined '%s'" % name)

    def set_func(self, name, val):
        if name in self.__table[self.__func]:
      
            raise DuplicateSymbol("Function cannot be declared '%s'" % name)

        self.__table[self.__func][name] = val
