# ANTLR4 Grammars for Python
1. Generate visitors and parsers using ANTLR4 in the visitors directory:
    ```sh
    antlr4 ./PythonLexer.g4 -visitor -no-listener -Dlanguage=Python3 -o ../csim/visitors
    antlr4 ./PythonParser.g4 -visitor -no-listener -Dlanguage=Python3 -o ../csim/visitors
    ```