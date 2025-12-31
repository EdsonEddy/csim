from PythonParserVisitor import PythonParserVisitor
from zss import Node
from antlr4 import TerminalNode

EXCLUDED_RULES = {
    # wrappers
    "Statement",
    "Statements",
    "Simple_stmts",
    "Simple_stmt",
    "Star_expression",
    "Star_expressions",
    "Function_def_raw",
    # precedence / expressions
    "Disjunction",
    "Conjunction",
    "Inversion",
    "Comparison",
    "Bitwise_or",
    "Bitwise_xor",
    "Bitwise_and",
    "Shift_expr",
    "Sum",
    "Term",
    "Factor",
    "Power",
    "Await_primary",
    "Primary",
    "Atom",
    # names
    "Name",
    "Name_except_underscore",
    # other technicals
    "Target_with_star_atom",
    "Star_atom",
    # collapse rules
    "Import_name",
    "Dotted_as_names",
    "Dotted_as_name",
    "Dotted_name",
}

EXCLUDED_TOKENS = {"(", ")", ":", ",", "<INDENT>", "<DEDENT>", "<EOF>"}


class ZssBuilderVisitor(PythonParserVisitor):

    def visitChildren(self, node):
        rule_name = type(node).__name__.replace("Context", "")
        children_nodes = []

        for child in node.getChildren():
            if isinstance(child, TerminalNode):
                text = child.getText()
                if text not in EXCLUDED_TOKENS and text.strip():
                    children_nodes.append(Node(f"TOKEN:{text}"))
            else:
                result = self.visit(child)
                if result is not None:
                    children_nodes.append(result)

        # 1. Rules to collapse completely
        if rule_name in EXCLUDED_RULES:
            if len(children_nodes) == 1:
                return children_nodes[0]
            elif len(children_nodes) > 1:
                group = Node("GROUP")
                for c in children_nodes:
                    group.addkid(c)
                return group
            else:
                return None

        # 2. Valid rule, create node
        zss_node = Node(rule_name)
        for c in children_nodes:
            zss_node.addkid(c)

        return zss_node


from antlr4 import *
from PythonParser import PythonParser
from PythonLexer import PythonLexer


def main():
    code_example = """
import os
import sys

def main():
    x = 5
    y = 10
    result = x + y
    print("The result is:", result)

if __name__ == "__main__":
    main()
"""

    input_stream = InputStream(code_example)
    lexer = PythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PythonParser(token_stream)

    # ANTLR tree
    tree = parser.file_input()

    # Visitor
    visitor = ZssBuilderVisitor()

    # ZSS tree
    zss_tree = visitor.visit(tree)

    def print_tree(node, indent=0):
        if node is None:
            return
        print("  " * indent + node.label)
        for child in node.children:
            print_tree(child, indent + 1)

    print_tree(zss_tree)


if __name__ == "__main__":
    main()
