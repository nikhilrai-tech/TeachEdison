# TechEdison

## Prerequisites

Ensure you have the following prerequisites installed before setting up the project:

- Python (version 3.9.13)
- Virtualenv
- MySQL server (and MySQL Workbench)
- IDE (VSCode recommended)

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nikhilrai-tech/TeachEdison.git
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Manually update the settings.py file for connecting to MySQL:**

    Open the `settings.py` file and update the `DATABASES` section:

    ```python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": 'Your_schema_name',
            "HOST": "127.0.0.1",
            "PORT": "3306",
            "USER": 'Your_username',
            "PASSWORD": 'Your_password',
            "OPTIONS": {"charset": "utf8mb4"},
        }
    }
    ```

    Replace 'Your_schema_name', 'Your_username', and 'Your_password' with your actual MySQL schema name, username, and password.

5. **Apply migrations:**

    Apply migrations using the following commands:

    ```bash
    python manage.py makemigrations bookstore reviews user
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The project will be accessible at http://localhost:8000/
