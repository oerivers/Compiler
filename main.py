import compiler

with open('test_files/test.mb', 'r') as file:
    compiler.execute(file.read())
