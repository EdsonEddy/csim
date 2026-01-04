from .PythonParser import PythonParser

GROUP_INDEX = 10**9

EXCLUDED_RULE_INDICES = {
    # wrappers
    PythonParser.RULE_statement,
    PythonParser.RULE_statements,
    PythonParser.RULE_simple_stmts,
    PythonParser.RULE_simple_stmt,
    PythonParser.RULE_star_expression,
    PythonParser.RULE_star_expressions,
    PythonParser.RULE_function_def_raw,
    # precedence / expressions
    PythonParser.RULE_disjunction,
    PythonParser.RULE_conjunction,
    PythonParser.RULE_inversion,
    PythonParser.RULE_comparison,
    PythonParser.RULE_bitwise_or,
    PythonParser.RULE_bitwise_xor,
    PythonParser.RULE_bitwise_and,
    PythonParser.RULE_shift_expr,
    PythonParser.RULE_sum,
    PythonParser.RULE_term,
    PythonParser.RULE_factor,
    PythonParser.RULE_power,
    PythonParser.RULE_await_primary,
    PythonParser.RULE_primary,
    PythonParser.RULE_atom,
    # names
    PythonParser.RULE_name,
    PythonParser.RULE_name_except_underscore,
    # other technicals
    PythonParser.RULE_target_with_star_atom,
    PythonParser.RULE_star_atom,
    # collapse (import)
    PythonParser.RULE_import_name,
    PythonParser.RULE_dotted_as_names,
    PythonParser.RULE_dotted_as_name,
    PythonParser.RULE_dotted_name,
}

from .PythonLexer import PythonLexer
from antlr4 import Token

EXCLUDED_TOKEN_TYPES = {
    PythonLexer.LPAR,
    PythonLexer.RPAR,
    PythonLexer.COLON,
    PythonLexer.COMMA,
    PythonLexer.INDENT,
    PythonLexer.DEDENT,
    Token.EOF,
}

import argparse
from pathlib import Path

# Utility functions for argument parsing


def get_file(file_path):
    if not Path(file_path).is_file():
        raise argparse.ArgumentTypeError(f"File '{file_path}' does not exist.")
    return file_path


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return file_path, content
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return file_path, None


def process_files(args):
    # Storage for file names and contents
    file_names = []
    file_contents = []
    # Process the files based on the provided arguments
    if args.files is not None:
        file1, file2 = args.files
        file_name1, content1 = read_file(file1)
        file_name2, content2 = read_file(file2)
        # Store the file name and content
        file_names.extend([file_name1, file_name2])
        file_contents.extend([content1, content2])

    return file_names, file_contents
