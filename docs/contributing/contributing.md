# Contributing to AIFlow

Thank you for your interest in contributing to AIFlow! This guide will help you get started with contributing to the project.

## Code of Conduct

Please read and follow our [Code of Conduct](https://github.com/kaushik701/AIFlow/blob/main/docs/contributing/code-of-conduct.md) to help us maintain a healthy and welcoming community.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- Git
- pip (Python package installer)

### Setting Up the Development Environment

1. **Fork the repository**:
   - Visit the [AIFlow repository](https://github.com/kaushik701/AIFlow) on GitHub
   - Click the "Fork" button in the upper right corner

2. **Clone your fork**:
   ```bash
   git clone https://github.com/kaushik701/AIFlow.git
   cd aiflow
   ```

3. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install development dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

## Development Workflow

### Creating a Branch

Create a new branch for your feature or bugfix:

```bash
git checkout -b feature/your-feature-name
```

Use a descriptive branch name that reflects the changes you're making.

### Making Changes

1. Make your changes to the codebase
2. Write or update tests for your changes
3. Run the tests to ensure they pass
4. Update documentation as needed

### Running Tests

Run the test suite to ensure your changes don't break existing functionality:

```bash
pytest
```

To run specific tests:

```bash
pytest tests/test_specific_file.py
```

### Code Style

We follow the PEP 8 style guide for Python code. Please ensure your code adheres to this standard.

You can use tools like `flake8` and `black` to check and format your code:

```bash
# Check code style
flake8 aiflow tests

# Format code
black aiflow tests
```

### Commit Guidelines

Write clear, concise commit messages that explain the changes you've made:

```
feat: Add support for new model provider

Add support for using the XYZ model provider in AIFlow workflows.
This includes:
- Implementation of XYZModelProvider class
- Integration with the interpreter
- Tests for the new provider
```

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages.

## Pull Request Process

1. **Update your fork**:
   ```bash
   git remote add upstream https://github.com/kaushik701/AIFlow.git
   git fetch upstream
   git merge upstream/main
   ```

2. **Push your changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a pull request**:
   - Go to the [AIFlow repository](https://github.com/kaushik701/AIFlow)
   - Click "New Pull Request"
   - Select "compare across forks"
   - Select your fork and branch
   - Fill out the pull request template with details about your changes

4. **Code review**:
   - Wait for maintainers to review your code
   - Address any feedback or requested changes
   - Update your branch as needed

5. **Merge**:
   - Once approved, a maintainer will merge your pull request

## Reporting Bugs

If you find a bug, please report it by creating an issue in the GitHub repository:

1. Check existing issues to see if the bug has already been reported
2. Use the bug report template to create a new issue
3. Include detailed steps to reproduce the bug
4. Include information about your environment (OS, Python version, etc.)

## Requesting Features

If you have an idea for a new feature, please create an issue in the GitHub repository:

1. Check existing issues to see if the feature has already been requested
2. Use the feature request template to create a new issue
3. Describe the feature in detail and explain why it would be valuable

## Documentation

Improving documentation is a valuable contribution! You can help by:

- Fixing typos or clarifying existing documentation
- Adding examples or tutorials
- Documenting new features
- Translating documentation to other languages

## Community

Join our community to get help, share ideas, and collaborate:

- [GitHub Discussions](https://github.com/kaushik701/AIFlow/discussions)
- [Discord Server](https://discord.gg/aiflow)

## License

By contributing to AIFlow, you agree that your contributions will be licensed under the project's [MIT License](../LICENSE).

## Thank You!

Your contributions help make AIFlow better for everyone. We appreciate your time and effort!
