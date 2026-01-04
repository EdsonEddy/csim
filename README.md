# Code Similarity (csim)

Code Similarity (csim) provide a module designed to detect similarities between source code files, even when obfuscation techniques have been applied. It is particularly useful for programming instructors and students who need to verify code originality.

## Key Features

- **Source Code Similarity Analysis:** Compares source code files to determine their degree of similarity.
- **Advanced Analysis:** Utilizes parse trees and the tree edit distance algorithm for in-depth analysis.
- **Parse Trees:** Represents the syntactic structure of source code, enabling detailed comparisons.
- **Tree Edit Distance:** Measures the similarity between different code structures.

## Technologies Used

- **Python:** The core programming language for the tool.
- **ANTLR:** A parser generator for creating parse trees from source code.
- **zss:** A library for calculating the tree edit distance.

## Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/EdsonEddy/csim.git
    ```
2.  Navigate to the project directory:
    ```sh
    cd csim
    ```
3.  Install the package:
    ```sh
    pip install .
    ```

## Usage

csim can be used from the command line as follows:
```sh
csim -f file1.py file2.py
```

Alternatively, you can use csim as a Python module:
```python
from csim import Compare
code_a = "a = 5"
code_b = "c = 50"
similarity = Compare(code_a, code_b)
print(f"Similarity: {similarity}")
```

## Parser Generation

This section describes how to regenerate the parser files using ANTLR 4. You do not need to follow these steps unless you intend to modify the grammar.

The Python parser files (e.g., `PythonLexer.py`, `PythonParser.py`, `PythonParserVisitor.py`) located in the `csim/` directory were generated using the ANTLR 4 tool. The grammar files (`PythonLexer.g4` and `PythonParser.g4`) were sourced from the [antlr/grammars-v4/python3_13](https://github.com/antlr/grammars-v4/tree/master/python/python3_13) repository.

To regenerate the files, run the following command from the `grammars/` directory:

```sh
antlr4 -Dlanguage=Python3 -visitor -o ../csim/ PythonLexer.g4 PythonParser.g4
```

This command instructs ANTLR to generate Python 3 code (`-Dlanguage=Python3`), create a visitor class (`-visitor`), and output the resulting files into the `../csim/` directory.

Additionally, we need download `PythonLexerBase.py` file from the ANTLR4 grammars GitHub repository and move them to the csim directory:
```sh
curl -O https://raw.githubusercontent.com/antlr/grammars-v4/master/python/python3_13/Python3/PythonLexerBase.py 
```

## Contributing

Contributions are welcome! To contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/new-feature`).
3.  Make your changes and commit them (`git commit -am 'Add new feature'`).
4.  Push to the branch (`git push origin feature/new-feature`).
5.  Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Links

- [Repository](https://github.com/EdsonEddy/csim)
- [Documentation](https://github.com/EdsonEddy/csim/wiki)
- [Report a Bug](https://github.com/EdsonEddy/csim/issues)

## Additional Resources

For more information on the techniques and tools used in this project, refer to the following resources:

- [ANTLR](https://www.antlr.org/)
- [Parse Tree (Wikipedia)](https://en.wikipedia.org/wiki/Parse_tree)
- [Tree Edit Distance (Wikipedia)](https://en.wikipedia.org/wiki/Tree_edit_distance)
- [zss (PyPI)](https://pypi.org/project/zss/)

## Third-Party Licenses

This project utilizes the following third-party libraries:

### ANTLR (ANother Tool for Language Recognition)
- **Purpose:** A parser generator used to create parse trees from source code.
- **License:** BSD 3-Clause
- **Website:** [https://www.antlr.org/](https://www.antlr.org/)
- **Repository:** [https://github.com/antlr/antlr4](https://github.com/antlr/antlr4)

### ANTLR4-parser-for-Python-3.14 by RobEin
- **Purpose:** Python 3.14 grammar for ANTLR4
- **License:** MIT License
- **Repository:** [https://github.com/RobEin/ANTLR4-parser-for-Python-3.14](https://github.com/RobEin/ANTLR4-parser-for-Python-3.14)

### zss (Zhang-Shasha)
- **Purpose:** Tree edit distance algorithm implementation for comparing tree structures
- **License:** MIT License
- **Repository:** [https://github.com/timtadh/zhang-shasha](https://github.com/timtadh/zhang-shasha)

