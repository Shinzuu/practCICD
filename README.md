# FastAPI Todo App with CI/CD

A simple Todo API built with FastAPI, tested with pytest, and deployed using GitHub Actions.

## Features

- RESTful API for managing todos
- Full test coverage
- CI/CD pipeline with GitHub Actions
- Code coverage reporting

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd practCICD
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

## Running Tests

```bash
# Run tests with coverage
pytest --cov=src

# Run tests with detailed output
pytest -v
```

## API Documentation

Once the application is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:
1. Runs tests on every push and pull request
2. Reports test coverage
3. Deploys the application on push to main (deployment steps need to be configured)

## Project Structure

```
practCICD/
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # GitHub Actions workflow
├── src/
│   └── main.py           # Main application code
├── tests/
│   └── test_todos.py     # Test cases
├── .gitignore
├── pytest.ini            # pytest configuration
├── README.md             # This file
└── requirements.txt      # Project dependencies
```

## License

MIT
