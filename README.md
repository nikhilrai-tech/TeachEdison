# TechEdison
## Prerequisites

- Python (version 3.9.13)

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

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The project will be accessible at http://localhost:8000/
