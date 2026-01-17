from .PythonParser import PythonParser
from .PythonLexer import PythonLexer
from .PythonParserVisitor import PythonParserVisitor
from .utils import EXCLUDED_TOKEN_TYPES, GROUP_INDEX, TOKEN_TYPE_OFFSET
from antlr4 import InputStream, CommonTokenStream, TerminalNode
from antlr4 import CommonTokenStream
from zss import simple_distance, Node


class Visitor(PythonParserVisitor):

    def __init__(self):
        super().__init__()
        self.node_count = 0

    def visitChildren(self, node):
        rule_index = node.getRuleIndex()
        children_nodes = []

        for child in node.getChildren():
            if isinstance(child, TerminalNode):
                token = child.symbol
                if token.type not in EXCLUDED_TOKEN_TYPES:
                    self.node_count += 1
                    # Offset token types to avoid collision with rule indices
                    token_type_index = token.type + TOKEN_TYPE_OFFSET
                    children_nodes.append(Node(token_type_index))
            else:
                result = self.visit(child)
                if result is not None:
                    children_nodes.append(result)

        # nodes compression
        if len(children_nodes) == 1:
            return children_nodes[0]
        elif len(children_nodes) > 1:
            self.node_count += 1
            group = Node(GROUP_INDEX)
            for c in children_nodes:
                group.addkid(c)
            return group

        self.node_count += 1
        zss_node = Node(rule_index)
        return zss_node

    """
    Special case: handle star_named_expressions to avoid excessive nodes
    e.g., [1, 2, 3, ..., k]
    """

    def visitStar_named_expressions(self, node):
        list_idx = node.getRuleIndex()
        self.node_count += 1
        return Node(list_idx)


def Normalize(tree):

    visitor = Visitor()
    normalized_tree = visitor.visit(tree)

    return normalized_tree, visitor.node_count


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


# Distance function for zss
def label_dist(a, b):
    return 0 if a == b else 1


def Compare(code_a, code_b):
    T1 = ANTLR_parse(code_a)
    T2 = ANTLR_parse(code_b)

    N1, len_N1 = Normalize(T1)
    N2, len_N2 = Normalize(T2)

    d = simple_distance(N1, N2, label_dist=label_dist)
    s = SimilarityIndex(d, len_N1, len_N2)
    return s
