# Student Management System

This is a Django-based web application for managing student records. It allows users to add, edit, delete, and view student information, along with user authentication features.

## Features

- User authentication (registration, login, logout)
- Add, edit, delete, and view student records
- Search functionality for students by name
- Pagination for student list display

## Prerequisites

- Python 3.x installed on your machine
- pip (Python package installer) installed
- Django installed (preferably in a virtual environment)

## Installation

1. **Clone the repository**:

    ```bash
   git clone https://github.com/p0ur1a/fullstack_web_development.git
   cd fullstack_web_development/week4/Assignment2
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - For Windows:

        ```bash
        venv\Scripts\activate
        ```

    - For macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply database migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser** (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser account.

## Running the Project

1. Start the development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and go to `http://127.0.0.1:8000/students/` to view the application.

## Usage

- **Register** an account to log in.
- Use the navigation to add, edit, or delete student records.
- Search for students by name using the search bar.
- View detailed information for each student.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
