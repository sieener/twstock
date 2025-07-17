# Modern Python 3 Development Standards

When developing Python applications, follow these modern Python 3 standards and best practices:

## Python Version and Compatibility
- Use Python 3.9+ as the minimum version (preferably Python 3.11+ for latest features)
- Use type hints throughout the codebase (`from __future__ import annotations` for Python 3.9-3.10)
- Leverage modern Python features like dataclasses, pathlib, f-strings, and structural pattern matching (3.10+)

## Code Style and Formatting
- Follow PEP 8 style guidelines
- Use `black` for automatic code formatting with line length of 88 characters
- Use `isort` for import sorting with black-compatible settings
- Use `flake8` or `ruff` for linting
- Configure pre-commit hooks for consistent formatting

## Type Safety
- Add type hints to all function signatures, class attributes, and variables where type is not obvious
- Use `mypy` for static type checking with strict configuration
- Use generic types from `typing` module (e.g., `List[str]`, `Dict[str, int]`)
- For Python 3.9+, use built-in collections for type hints (e.g., `list[str]`, `dict[str, int]`)
- Use `TypedDict`, `Protocol`, and `Union`/`Optional` types appropriately

## Project Structure and Dependencies
- Use `pyproject.toml` for project configuration (PEP 621)
- Use virtual environments (venv, conda, or poetry)
- Pin dependencies with version ranges in `pyproject.toml`
- Use `poetry` or `pip-tools` for dependency management
- Separate development dependencies from runtime dependencies

## Code Quality and Testing
- Write comprehensive unit tests using `pytest`
- Aim for >90% test coverage using `coverage.py`
- Use `pytest-cov` for coverage reporting
- Write docstrings for all public functions, classes, and modules (Google or NumPy style)
- Use `pydocstyle` for docstring linting

## Modern Python Patterns
- Use dataclasses or Pydantic models for data structures
- Prefer pathlib over os.path for file operations
- Use context managers (with statements) for resource management
- Use f-strings for string formatting instead of % or .format()
- Use list/dict comprehensions and generator expressions appropriately
- Use `match-case` statements (Python 3.10+) for complex conditionals

## Error Handling and Logging
- Use specific exception types, not bare `except:`
- Create custom exception classes when appropriate
- Use the `logging` module instead of print statements
- Configure structured logging with appropriate log levels
- Use `try-except-else-finally` blocks appropriately

## Performance and Best Practices
- Use `asyncio` for asynchronous programming when dealing with I/O operations
- Profile code with `cProfile` or `line_profiler` when performance matters
- Use `functools.lru_cache` for expensive function calls
- Prefer generator expressions over list comprehensions for large datasets
- Use `__slots__` for classes with many instances to save memory

## Security
- Never hardcode secrets or credentials
- Use environment variables or secret management systems
- Validate all external inputs
- Use `secrets` module for cryptographically secure random numbers
- Keep dependencies updated and scan for vulnerabilities

## Documentation
- Write clear README.md with installation and usage instructions
- Use type hints as inline documentation
- Write comprehensive docstrings with examples
- Consider using Sphinx for API documentation
- Include code examples in documentation

## Package Structure Example
```
project/
├── pyproject.toml          # Project configuration
├── README.md               # Project documentation
├── .gitignore             # Git ignore rules
├── .pre-commit-config.yaml # Pre-commit hooks
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── main.py
│       └── modules/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_*.py
└── docs/
    └── ...
```

## Development Tools Configuration
- Configure your IDE/editor with Python language server (Pylsp, Pyright, or similar)
- Use automatic import sorting and formatting on save
- Set up linting and type checking in your editor
- Use debugging tools and interactive Python shells (IPython, pdb)

## Modern Dependencies to Consider
- **pydantic**: Data validation and parsing
- **fastapi**: Modern web framework (if building APIs)
- **httpx**: Modern HTTP client (async/sync)
- **typer**: Modern CLI framework
- **rich**: Rich text and beautiful formatting
- **structlog**: Structured logging
- **pytest-asyncio**: Testing async code

Follow these standards to ensure your Python code is maintainable, readable, and follows modern best practices.
