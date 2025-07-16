# Contributing to MongoDB Atlas Charts POC

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the MongoDB Atlas Charts POC repository.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Style Guidelines](#style-guidelines)
- [Documentation](#documentation)

## 🤝 Code of Conduct

This project adheres to a code of conduct that promotes a welcoming and inclusive environment:

- Be respectful and considerate in all interactions
- Focus on constructive feedback and collaboration
- Respect different viewpoints and experiences
- Help maintain a harassment-free environment

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- MongoDB Atlas account (for testing)
- Basic knowledge of MongoDB and data visualization

### Development Setup

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/yourusername/mongodb-charts-poc.git
   cd mongodb-charts-poc
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Run tests to verify setup**
   ```bash
   pytest
   ```

## 🔧 Making Changes

### Branch Naming

Use descriptive branch names:
- `feature/add-new-chart-type`
- `bugfix/fix-connection-timeout`
- `docs/update-readme`
- `refactor/improve-data-generation`

### Commit Messages

Follow conventional commit format:
```
type(scope): description

Examples:
feat(data): add real-time streaming data generation
fix(charts): resolve auto-refresh timing issue
docs(readme): update installation instructions
test(generator): add unit tests for sales data
```

### Development Workflow

1. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, readable code
   - Follow existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**
   ```bash
   # Run all tests
   pytest
   
   # Run specific test file
   pytest tests/test_data_generation.py
   
   # Run with coverage
   pytest --cov=. --cov-report=html
   ```

4. **Format your code**
   ```bash
   black mongodb_data_generator.py
   flake8 .
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat(data): add new chart type support"
   ```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test category
pytest tests/test_data_generation.py::TestMongoDataGenerator

# Run with coverage report
pytest --cov=. --cov-report=html
```

### Writing Tests

- Place tests in the `tests/` directory
- Use descriptive test names
- Include both positive and negative test cases
- Mock external dependencies (MongoDB connections)
- Test edge cases and error conditions

Example test structure:
```python
def test_generate_sales_data_with_valid_input(self, data_generator):
    """Test that sales data generation works with valid input."""
    # Arrange
    num_records = 10
    
    # Act
    result = data_generator.generate_sales_data(num_records)
    
    # Assert
    assert result is not None
    assert data_generator.db.sales_data.insert_many.called
```

### Test Categories

- **Unit Tests**: Test individual functions and methods
- **Integration Tests**: Test component interactions
- **Performance Tests**: Test performance characteristics
- **Error Handling Tests**: Test error conditions and recovery

## 📤 Submitting Changes

### Pull Request Process

1. **Update documentation**
   - Update README.md if needed
   - Add docstrings to new functions
   - Update examples if applicable

2. **Ensure tests pass**
   ```bash
   pytest
   black --check .
   flake8 .
   ```

3. **Create pull request**
   - Use a descriptive title
   - Include a detailed description
   - Reference any related issues
   - Add screenshots for UI changes

### Pull Request Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tests pass locally
- [ ] Added new tests for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
```

## 🎨 Style Guidelines

### Python Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused
- Use type hints where appropriate

Example:
```python
def generate_sales_data(self, num_records: int) -> Collection:
    """Generate realistic sales data for visualization.
    
    Args:
        num_records: Number of sales records to generate
        
    Returns:
        MongoDB collection containing the generated data
        
    Raises:
        ValueError: If num_records is negative
    """
    if num_records < 0:
        raise ValueError("Number of records must be non-negative")
    
    # Implementation...
```

### Documentation Style

- Use clear, concise language
- Include code examples
- Add screenshots for UI features
- Use markdown formatting consistently
- Keep documentation up-to-date

## 📖 Documentation

### Types of Documentation

1. **Code Documentation**
   - Docstrings for all functions/classes
   - Inline comments for complex logic
   - Type hints for better IDE support

2. **User Documentation**
   - README.md updates
   - Setup instructions
   - Usage examples
   - Troubleshooting guides

3. **Developer Documentation**
   - Architecture decisions
   - Development setup
   - Testing guidelines
   - Deployment procedures

### Documentation Standards

- Use clear, concise language
- Include practical examples
- Test all code examples
- Update documentation with code changes
- Use proper markdown formatting

## 🔍 Code Review Process

### For Contributors

- Respond to review comments promptly
- Make requested changes in separate commits
- Ask questions if feedback is unclear
- Be open to suggestions and improvements

### For Reviewers

- Be constructive and specific
- Explain the reasoning behind suggestions
- Acknowledge good code practices
- Focus on code quality and maintainability

## 📊 Performance Considerations

When contributing performance-related changes:

- Profile code before and after changes
- Consider memory usage and CPU impact
- Test with realistic data volumes
- Document performance improvements
- Add performance tests for critical paths

## 🚨 Security Guidelines

- Never commit sensitive data (connection strings, passwords)
- Use environment variables for configuration
- Validate all user inputs
- Follow secure coding practices
- Report security issues privately

## 🆘 Getting Help

- **Issues**: Create GitHub issues for bugs and feature requests
- **Discussions**: Use GitHub discussions for questions
- **Documentation**: Check existing documentation first
- **Community**: Engage with other contributors respectfully

## 📝 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to MongoDB Atlas Charts POC! 🙏