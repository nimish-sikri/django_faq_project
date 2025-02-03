# FAQ Project

A multilingual FAQ management system built using Django and Django REST Framework (DRF), supporting multiple languages using automatic translation.

## Features

- Manage FAQs via Django Admin Panel.
- API endpoints for fetching FAQs.
- Automatic translation support for multiple languages.
- Caching for optimized performance.
- Docker support for easy deployment.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.
- 12+
- pip (Python package manager)
- PostgreSQL or SQLite (for database management)
- Docker (optional, for containerized deployment)

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/faq_project.git
   cd faq_project
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```sh
   cp .env.example .env  # Modify .env with your credentials
   ```
5. Apply migrations and create a superuser:
   ```sh
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Usage

### Get all FAQs

```sh
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

### Get FAQs in Hindi (hi)

```sh
GET /api/faqs/?lang=hi
```

Response:

```json
[
  {
    "id": 1,
    "question": "Django क्या है?",
    "answer": "Django एक उच्च-स्तरीय पायथन वेब फ्रेमवर्क है।"
  }
]
```

## Contribution Guidelines

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```sh
   git checkout -b feature-new-translation
   ```
3. Commit your changes:
   ```sh
   git commit -m "feat: Add support for new language"
   ```
4. Push to GitHub:
   ```sh
   git push origin feature-new-translation
   ```
5. Submit a Pull Request.

## Deployment with Docker

### Build and Run with Docker

```sh
docker-compose up --build
```

### Deploy to Heroku (Optional)

1. Install the Heroku CLI.
2. Login to Heroku:
   ```sh
   heroku login
   ```
3. Create a Heroku app and deploy:
   ```sh
   heroku create your-faq-app
   git push heroku main
   ```



