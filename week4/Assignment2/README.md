# Student Management System

This is a Django-based web application for managing student records. It allows users to add, edit, delete, and view student information, along with user authentication features.

## Features

- User authentication (registration, login, logout)
- Add, edit, delete, and view student records
- Search functionality for students by name
- Pagination for student list display
- Data verification for various data fields

## Prerequisites

- Python 3.x
- Django 3.x
- pip (Python package installer)
- Git

## Installation

1. **Clone the repository**:

    ```bash
   git clone https://github.com/p0ur1a/fullstack_web_development.git
   cd fullstack_web_development/week4/Assignment2
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. **Install Django**:
    ```bash
    pip install django
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

## Running the Project

1. Start the development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Register** an account to log in.
- Use the navigation to add, edit, or delete student records.
- Search for students by name using the search bar.
- View detailed information for each student.

## License

This project is licensed under the MIT License.
