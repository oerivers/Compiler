import operator
from types import LambdaType

class InstructionList:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children

    def __len__(self):
        return len(self.children)

    def __iter__(self):
        return iter(self.children)

    def __repr__(self):
        return '<InstructionList {0}>'.format(self.children)

    def eval(self):

        ret = []
        for n in self:
            if isinstance(n, ExitStatement):
                return n

            res = n.eval()

            if isinstance(res, ExitStatement):
                return res
            elif res is not None:
                ret.append(res)

        return ret


class BaseExpression:
    def eval(self):
        raise NotImplementedError()


class ExitStatement(BaseExpression):
    def __iter__(self):
        return []

    def eval(self):
        pass


class Primitive(BaseExpression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<Primitive "{0}"({1})>'.format(self.value, self.value.__class__)

    def eval(self):
        return self.value



class Identifier(BaseExpression):
    is_function = False

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Identifier {0}>'.format(self.name)

    def assign(self, val):
        if self.is_function:
            symbols.set_func(self.name, val)
        else:
            symbols.set_sym(self.name, val)
    # need
    def eval(self):
        if self.is_function:
            return symbols.get_func(self.name)

        return symbols.get_sym(self.name)


class Assignment(BaseExpression):
    def __init__(self, identifier: Identifier, val):
        self.identifier = identifier
        self.val = val

    def __repr__(self):
        return '<Assignment sym={0}; val={1}>'.format(self.identifier, self.val)

    # first call after finishing the enviroment file
    def eval(self):
        if self.identifier.is_function:
            self.identifier.assign(self.val)
        else:
            self.identifier.assign(self.val.eval())


class BinaryOperation(BaseExpression):
    __operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '^': operator.pow,
        '/': operator.truediv,
        '%': operator.mod,

        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,

        'and': lambda a, b: a.eval() and b.eval(),
        'or': lambda a, b: a.eval() or b.eval(),

    }
    

    def __repr__(self):
        return '<BinaryOperation left ={0} right={1} operation="{2}">'.format(self.left, self.right, self.op)

    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op

    def eval(self):
        left = None
        right = None

        try:
            op = self.__operations[self.op]
            if isinstance(op, LambdaType):
                return op(self.left, self.right)

            left = self.left.eval()
            right = self.right.eval()
            return op(left, right)
        except TypeError:
            fmt = (left.__class__.__name__, left, self.op, right.__class__.__name__, right)
            raise InterpreterRuntimeError("Unable to apply operation (%s: %s) %s (%s: %s)" % fmt)


class UnaryOperation(BaseExpression):
    __operations = {
        '+': operator.pos,
        '-': operator.neg,
    }

    def __repr__(self):
        return '<Unary operation: operation={0} expr={1}>'.format(self.operation, self.expr)

    def __init__(self, operation, expr: BaseExpression):
        self.operation = operation
        self.expr = expr

    def eval(self):
        return self.__operations[self.operation](self.expr.eval())


class If(BaseExpression):
    def __init__(self, condition: BaseExpression, truepart: InstructionList, elsepart=None):
        self.condition = condition
        self.truepart = truepart
        self.elsepart = elsepart

    def __repr__(self):
        return '<If condition={0} then={1} else={2}>'.format(self.condition, self.truepart, self.elsepart)

    def eval(self):
        if self.condition.eval():
            return self.truepart.eval()
        elif self.elsepart is not None:
            return self.elsepart.eval()


class ForIn(BaseExpression):
    def __init__(self, variable: Identifier, sequence: BaseExpression, body: InstructionList):
        self.variable = variable
        self.sequence = sequence
        self.body = body

    def __repr__(self):
        return '<ForIn var={0} in iterable={1} do body={2}>'.format(self.variable, self.sequence, self.body)

    def eval(self):
        for i in self.sequence.eval():
            self.variable.assign(i)
            if isinstance(self.body.eval(), ExitStatement):
                break


class While(BaseExpression):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return '<While cond={0} body={1}>'.format(self.condition, self.body)

    def eval(self):
        while self.condition.eval():
            if isinstance(self.body.eval(), ExitStatement):
                break


class PrintStatement(BaseExpression):
    def __init__(self, items: InstructionList):
        self.items = items

    def __repr__(self):
        return '<Print {0}>'.format(self.items)

    def eval(self):
        print(*self.items.eval(), end='', sep='')


class FunctionCall(BaseExpression):
    def __init__(self, name: Identifier, params: InstructionList):
        self.name = name
        self.params = params

    def __repr__(self):
        return '<Function call name={0} params={1}>'.format(self.name, self.params)

    def __eval_builtin_func(self):
        func = self.name.eval()
        args = []
        return func.eval(args)

    def __eval_udf(self):
        func = self.name.eval()
        args = {}
        return func.eval(args)

    def eval(self):
        if isinstance(self.name.eval(), BuiltInFunction):
            return self.__eval_builtin_func()

        return self.__eval_udf()


class Function(BaseExpression):
    def __init__(self, params: InstructionList, body: InstructionList):
        self.params = params
        self.body = body

    def __repr__(self):
        return '<Function params={0} body={1}>'.format(self.params, self.body)


    def eval(self, args):
        symbols.set_local(True)

        for k, v in args.items():
            symbols.set_sym(k, v)

        try:
            ret = self.body.eval()

        finally:
            symbols.set_local(False)

        return None


class BuiltInFunction(BaseExpression):
    def __init__(self, func):
        self.func = func

    def __repr__(self):
        return '<Builtin function {0}>'.format(self.func)

    def eval(self, args):
        return self.func(*args)
