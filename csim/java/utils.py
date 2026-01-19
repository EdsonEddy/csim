from .Java20Lexer import Java20Lexer
from .Java20Parser import Java20Parser
from antlr4 import Token

EXCLUDED_RULE_INDICES = {
    Java20Parser.RULE_classModifier,
    Java20Parser.RULE_typeIdentifier,
    Java20Parser.RULE_fieldModifier,
    Java20Parser.RULE_unannPrimitiveType,
    Java20Parser.RULE_unannType,
    Java20Parser.RULE_primitiveType,
    Java20Parser.RULE_unannClassOrInterfaceType,
    Java20Parser.RULE_methodModifier,
}

COLLAPSED_RULE_INDICES = {
    Java20Parser.RULE_singleTypeImportDeclaration,
    Java20Parser.RULE_variableInitializerList,
    Java20Parser.RULE_dims,
    Java20Parser.RULE_dimExpr,
}

EXCLUDED_TOKEN_TYPES = {
    Java20Lexer.LPAREN,
    Java20Lexer.RPAREN,
    Java20Lexer.LBRACE,
    Java20Lexer.RBRACE,
    Java20Lexer.COLON,
    Java20Lexer.COMMA,
    Java20Lexer.SEMI,
    Java20Lexer.Identifier,
    # Keywords that do not contribute to structural similarity
    Java20Lexer.PUBLIC,
    Java20Lexer.CLASS,
    Java20Lexer.STATIC,
    Java20Lexer.NEW,
    Java20Lexer.VOID,
    # Keywords related to data types
    Java20Lexer.INT,
    Java20Lexer.BOOLEAN,
    Java20Lexer.BYTE,
    Java20Lexer.CHAR,
    Java20Lexer.DOUBLE,
    Java20Lexer.FLOAT,
    Java20Lexer.LONG,
    Java20Lexer.SHORT,
    Java20Lexer.IntegerLiteral,
    Java20Lexer.FloatingPointLiteral,
    Java20Lexer.BooleanLiteral,
    Java20Lexer.CharacterLiteral,
    Java20Lexer.StringLiteral,
    # Whitespace and comments
    Token.EOF,
}
