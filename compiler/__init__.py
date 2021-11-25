import compiler.parser as p
import compiler.compiler_ast
import compiler.exceptions
import sys


def execute(source, show_ast: bool=False, disable_warnings: bool=True):
    p.disable_warnings = disable_warnings

    try:
        res = p.get_parser().parse(source)
        f = comp_ast.BuiltInFunction
        comp_final.comp_ast.symbols.set_func('int', f(int))
        comp_final.comp_ast.symbols.set_func('float', f(float))
        comp_final.comp_ast.symbols.set_func('ask', f(input))

        for node in res.children:
            node.eval()

    except Exception as e:
        print(e.__class__.__name__ + ': ' + str(e), file=sys.stderr)
        if not disable_warnings:
            raise e
