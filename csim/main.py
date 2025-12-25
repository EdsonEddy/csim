from antlr4 import *
from zss import simple_distance, Node
from PythonParser import PythonParser
from PythonLexer import PythonLexer
from PythonParserVisitor import PythonParserVisitor


class NormNode(Node):

    def __init__(self, label):
        super().__init__(label)

    def addkid(self, node, before=False):
        if before:
            self.children.insert(0, node)
        else:
            self.children.append(node)
        return self


class NormalizationVisitor(PythonParserVisitor):

    def visitChildren(self, ctx):
        parent = None

        for child in ctx.children:
            node = self.visit(child)

            if node is None:
                continue

            if parent is None:
                parent = node
            else:
                parent.addkid(node)

        return parent

    def visitFile_input(self, ctx):
        root = NormNode("ROOT")
        for child in ctx.children:
            node = self.visit(child)
            if node:
                root.addkid(node)
        return root

    def visitFunction_def(self, ctx):
        node = NormNode("FUNCTION")
        for c in ctx.children:
            child = self.visit(c)
            if child:
                node.addkid(child)
        return node

    def visitName(self, ctx):
        return NormNode("IDENT")

    def visitAtom(self, ctx):
        if ctx.NUMBER() or ctx.strings():
            return NormNode("LITERAL")
        return self.visitChildren(ctx)


def main():
    code_example = """
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
    tree = parser.file_input()

    visitor = NormalizationVisitor()
    norm_tree = visitor.visit(tree)

    def print_tree(node, indent=0):
        if node is None:
            return
        print("  " * indent + node.label)
        for child in node.children:
            print_tree(child, indent + 1)

    print_tree(norm_tree)


if __name__ == "__main__":
    main()
