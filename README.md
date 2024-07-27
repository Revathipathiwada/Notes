# Notes App

## Description
A simple notes application with a frontend built using HTML, CSS, and JavaScript, and a backend powered by Django with an SQLite database.

## Installation

### Prerequisites
- Python 3.x and pip
- Django
- Git (optional, for version control)

### Frontend Setup
Ensure that your HTML files are properly structured and reference the necessary CSS and JavaScript files.

### Backend Setup
1. **Navigate to the backend directory:**
   cd path/to/your/django/project
2.Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install the required dependencies:
  pip install -r requirements.txt
4.Apply the database migrations:
  python manage.py migrate
5.Create a superuser:
  python manage.py createsuperuser
6.Run the Django development server:
  python manage.py runserver

### Integrating Frontend with Backend
Place your HTML files in the templates directory within the Django project.
Ensure that the Django settings are configured to serve templates correctly.
Update the URL configuration to route to the appropriate HTML templates for different endpoints.

### Running the Application
1.Start the Django development server to serve both the frontend and backend:
  python manage.py runserver
2.Open a web browser and navigate to the local server address (e.g., (http://127.0.0.1:8000/)) to access the application.
