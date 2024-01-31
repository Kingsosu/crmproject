# CRM System

Welcome to CRM System, a web application for managing customer relationships. This system empowers businesses to streamline their customer interactions and enhance overall customer satisfaction.

## Features

- **User Authentication:**
  - Users can create accounts and log in to access CRM functionalities.

- **Password Management:**
  - Password reset functionality for forgotten passwords.
  - Users can change their passwords securely.

- **Record Management:**
  - CRUD operations on customer records.
  - Add new records, update existing ones, and delete records.

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Kingsosu/crmsystem.git
    cd crmsystem
    ```

2. **Set up your virtual environment:**

    ```bash
    virtualenv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the application:**
    
    ```bash
    python manage.py runserver
    ```
