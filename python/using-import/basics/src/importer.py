# Example 1: Run as script.
# shell command: python src/importer.py
# from app import importable_function as imported_function

# imported_function()

# Example 2: Run as module.
# shell command: python -m src.importer
# from src.app import importable_function as imported_function

# imported_function()

# Example 3: Run as module.
# shell command: cd src && python -m src.importer
from app import importable_function as imported_function

imported_function()
