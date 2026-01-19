from .python.PythonParserVisitor import PythonParserVisitor
from .java.Java20ParserVisitor import Java20ParserVisitor
from zss import Node
from antlr4 import TerminalNode
from .java.utils import (
    EXCLUDED_RULE_INDICES as JAVA_EXCLUDED_RULES,
    COLLAPSED_RULE_INDICES as JAVA_COLLAPSED_RULES,
)
from .python.utils import (
    EXCLUDED_RULE_INDICES as PYTHON_EXCLUDED_RULES,
    COLLAPSED_RULE_INDICES as PYTHON_COLLAPSED_RULES,
)


class PythonParserVisitorExtended(PythonParserVisitor):

    def visit(self, tree):
        """Override visit to exclude certain rules from being processed.
        This helps in reducing noise in the parse tree by skipping over
        less relevant constructs.
        """
        if (
            not isinstance(tree, TerminalNode)
            and tree.getRuleIndex() in PYTHON_EXCLUDED_RULES
        ):
            return None
        elif (
            not isinstance(tree, TerminalNode)
            and tree.getRuleIndex() in PYTHON_COLLAPSED_RULES
        ):
            list_idx = tree.getRuleIndex()
            self.node_count += 1
            return Node(list_idx)
        return tree.accept(self)


class Java20ParserVisitorExtended(Java20ParserVisitor):

    def visit(self, tree):
        """Override visit to exclude certain rules from being processed.
        This helps in reducing noise in the parse tree by skipping over
        less relevant constructs.
        """
        if (
            not isinstance(tree, TerminalNode)
            and tree.getRuleIndex() in JAVA_EXCLUDED_RULES
        ):
            return None
        elif (
            not isinstance(tree, TerminalNode)
            and tree.getRuleIndex() in JAVA_COLLAPSED_RULES
        ):
            list_idx = tree.getRuleIndex()
            self.node_count += 1
            return Node(list_idx)
        return tree.accept(self)
