from PythonParser import PythonParser
from PythonLexer import PythonLexer
from antlr4 import InputStream
from antlr4 import CommonTokenStream
from utils import Normalize
from zss import simple_distance


def ANTLR_parse(code):
    input_stream = InputStream(code)
    lexer = PythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PythonParser(token_stream)
    tree = parser.file_input()
    return tree


def SimilarityIndex(d, T1, T2):
    m = max(T1, T2)
    s = 1 - (d / m)
    return s


def Compare(code_a, code_b):
    T1 = ANTLR_parse(code_a)
    T2 = ANTLR_parse(code_b)

    N1, len_N1 = Normalize(T1)
    N2, len_N2 = Normalize(T2)

    d = simple_distance(N1, N2)
    s = SimilarityIndex(d, len_N1, len_N2)
    return s


code_a = "a = 5"
code_b = "b = 5"
similarity = Compare(code_a, code_b)
print(f"Similarity: {similarity}")
