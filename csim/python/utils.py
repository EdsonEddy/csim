from .PythonParser import PythonParser
from .PythonLexer import PythonLexer
from antlr4 import Token

EXCLUDED_RULE_INDICES = {}

COLLAPSED_RULE_INDICES = {
    PythonParser.RULE_star_named_expressions,
}

EXCLUDED_TOKEN_TYPES = {
    PythonLexer.LPAR,
    PythonLexer.RPAR,
    PythonLexer.COLON,
    PythonLexer.COMMA,
    PythonLexer.INDENT,
    PythonLexer.DEDENT,
    PythonLexer.NEWLINE,
    Token.EOF,
}
