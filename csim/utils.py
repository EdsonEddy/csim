from PythonParserVisitor import PythonParserVisitor
from antlr4 import TerminalNode
from zss import Node

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


class Visitor(PythonParserVisitor):

    def __init__(self):
        super().__init__()
        self.node_count = 0

    def visitChildren(self, node):
        rule_name = type(node).__name__.replace("Context", "")
        children_nodes = []

        for child in node.getChildren():
            if isinstance(child, TerminalNode):
                text = child.getText()
                if text not in EXCLUDED_TOKENS and text.strip():
                    self.node_count += 1
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
                self.node_count += 1
                group = Node("GROUP")
                for c in children_nodes:
                    group.addkid(c)
                return group
            else:
                return None

        # 2. Valid rule, create node
        self.node_count += 1
        zss_node = Node(rule_name)
        for c in children_nodes:
            zss_node.addkid(c)

        return zss_node


def Normalize(tree):

    visitor = Visitor()
    normalized_tree = visitor.visit(tree)

    return normalized_tree, visitor.node_count
