# Django Backend Project Setup

This guide provides step-by-step instructions to set up and run the Django backend project locally. The project uses MySQL as the database and requires a virtual environment for dependency management.

## Prerequisites

- Python 3.8 or higher
- MySQL Server 8.0 or higher
- Git
- pip (Python package manager)
- Virtualenv (optional, but recommended)

## Setup Instructions

### 1. Clone the Repository

Clone the project from GitHub to your local machine:

```bash
git clone https://github.com/medamineharbaoui/training_management.git
cd your-repo-name
```


### 2. Set Up a Virtual Environment

Create and activate a virtual environment to isolate project dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Project Dependencies

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```


### 4. Install and Configure MySQL

1. **Install MySQL Server**:
   - Download and install MySQL Server from [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/).
   - Follow the installation instructions for your operating system.
   - Note the root username and password during installation.

2. **Install MySQL Client for Python**:
   Ensure `mysqlclient` is installed (included in `requirements.txt`). If you encounter issues, you may need to install MySQL development libraries:
   - On macOS:
     ```bash
     brew install mysql
     ```
   - On Ubuntu/Debian:
     ```bash
     sudo apt-get install libmysqlclient-dev
     ```
   - On Windows, use a precompiled `mysqlclient` wheel or follow the instructions at [https://pypi.org/project/mysqlclient/](https://pypi.org/project/mysqlclient/).

3. **Create the Database**:
   Log in to MySQL and create a database named `training_db`:
   ```bash
   mysql -u root -p
   ```
   Enter your MySQL root password, then run:
   ```sql
   CREATE DATABASE training_db;
   ```
   Exit the MySQL prompt:
   ```sql
   EXIT;
   ```

### 5. Configure the .env File

Create a `.env` file in the project root directory to store environment-specific settings:

```bash
touch .env
```

Add the following content to `.env`, replacing placeholders with your MySQL credentials and other settings:

```
DATABASE_NAME=training_db
DATABASE_USER=your_mysql_username
DATABASE_PASSWORD=your_mysql_password
DATABASE_HOST=localhost
DATABASE_PORT=3306
SECRET_KEY=your_django_secret_key
DEBUG=True
```

- Replace `your_mysql_username` and `your_mysql_password` with your MySQL credentials.
- Generate a secure `SECRET_KEY` for Django (e.g., using an online generator or `django.core.management.utils.get_random_secret_key()`).
- Keep the `.env` file secure and do not commit it to version control.

Update your Django `settings.py` to load these environment variables (example configuration):

```python
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}
```

### 6. Run Database Migrations

Apply the database migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`. Open this URL in your browser to verify the application is running.

Documentation on `http://127.0.0.1:8000/api/docs/`

## Troubleshooting

- **MySQL Connection Issues**: Ensure MySQL server is running and the credentials in `.env` are correct.
- **Missing Dependencies**: If `pip install -r requirements.txt` fails, ensure all dependencies are compatible with your Python version.
- **Permission Issues**: Ensure you have write permissions in the project directory for migrations and logs.

## Contributing

To contribute to this project, please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.