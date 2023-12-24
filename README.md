# TechEdison
## Prerequisites

- Python (version 3.9.13)
- Virtualenv
- MySql server (and / My SQL workbench)
- IDE (vscode)
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

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
5.**Manually update the settings.py file for connecting the mysql:**
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        **"NAME": 'Your_schema_name',**
        "HOST": "127.0.0.1",
        "PORT": "3306",
        **"USER": 'Your_username',**
        **"PASSWORD": 'Your_password',**
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

5. **Apply migrations:**

 Do the migrations using below commands 

python manage.py makemigrations bookstore reviews user

python3 manage.py migrate



6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The project will be accessible at http://localhost:8000/
