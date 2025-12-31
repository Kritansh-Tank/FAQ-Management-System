# FAQ Management System

This project is a Django-based FAQ Management System that provides an API for storing, retrieving, and translating frequently asked questions. It integrates caching for efficient data retrieval and uses CKEditor for rich-text answers.

## Installation

### Prerequisites

1. Python 3.8+
2. Django 4+
3. Virtual environment (recommended)

### Steps

1. Clone the repository: 
```bash
git clone https://github.com/Kritansh-Tank/FAQ-Management-System.git
cd FAQ-Management-System
```

2. Create and activate a virtual environment: 
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

## API Usage

### Retrieve FAQs 

```bash
GET /api/faqs/
```

Response: 
```json
[
    {
        "id": 1,
        "question": "What is Django?",
        "answer": "Django is a high-level Python web framework."
    }
]
```

### Create an FAQ Entry

```bash
POST /api/faqs/
Content-Type: application/json
```

Request Body: 
```json
{
    "question": "What is Python?",
    "answer": "Python is a versatile programming language."
}
```

### Retrieve FAQ Translation

```bash
GET /api/faqs/{id}/translation/?lang=hi
```

Response: 
```json
{
    "question": "डिजैंगो क्या है?",
    "answer": "डिजैंगो एक उच्च-स्तरीय पायथन वेब फ्रेमवर्क है।"
}
```

## Contribution Guidelines

### How to Contribute

1. Fork the repository.
2. Create a feature branch:
```bash
git checkout -b feature-new-functionality
```

3. Commit your changes: 
```bash
git commit -m "Added new functionality"
```

4. Push to your fork: 
```bash
git push origin feature-new-functionality
```

5. Open a Pull Request (PR) against the main branch.

## Code Style

1. Follow PEP8 for Python code.
2. Use flake8 for linting:
```bash
flake8
```

3. Ensure all tests pass before submitting a PR:
```bash
pytest
```
