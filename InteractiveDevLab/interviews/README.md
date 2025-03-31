# Hands-On Coding Mock Interview

## Overview
This mock interview is designed to test and enhance your skills in:
- **Object-Oriented Programming (OOP) in Python**
- **Databases using MySQL**
- **Flask for web development**
- **Frontend basics with HTML & CSS**

You will build a small web application where users can register, log in, and complete tasks. The challenge will be divided into multiple parts, each testing different concepts.

## Project Structure

```
mock_interview/
|-- app/
|   |-- models/
|   |   |-- user.py
|   |   |-- task.py
|   |-- routes/
|   |   |-- auth.py
|   |   |-- tasks.py
|   |-- templates/
|   |   |-- index.html
|   |   |-- dashboard.html
|   |-- static/
|   |   |-- styles.css
|   |-- __init__.py
|-- database/
|   |-- schema.sql
|-- tests/
|-- run.py
|-- README.md
```

## Key Components
### 1. Object-Oriented Programming (OOP) in Python
- **User and Task models**: Implement `User` and `Task` classes with appropriate attributes and methods.
- **Encapsulation**: Use private attributes and getters/setters where necessary.
- **Inheritance**: If needed, create a base class for shared logic.

### 2. MySQL Database
- Create a database schema with tables for users and tasks.
- Implement CRUD (Create, Read, Update, Delete) operations.
- Use SQLAlchemy or raw MySQL queries to interact with the database.

### 3. Flask
- Implement user authentication (registration & login system) using Flask.
- Use Flask Blueprints to organize routes.
- Render templates using Jinja2.

### 4. HTML & CSS
- Create a simple and responsive user interface.
- Design a basic dashboard where users can see and manage their tasks.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/evisp/mock_interview.git
   cd mock_interview
   ```
2. Initialize the database:
   ```bash
   mysql -u root -p < database/schema.sql
   ```
4. Run the Flask application:
   ```bash
   python run.py
   ```
5. Open the browser and navigate to `http://127.0.0.1:5000/`

