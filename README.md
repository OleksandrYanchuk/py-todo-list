# Django To-Do List App

This is a simple Django application that allows you to create and manage your to-do list. It provides functionality to create tasks, assign tags to tasks, update task details, mark tasks as done or undone, and delete tasks and tags.

## Setup and Local Installation

### To set up and run the project locally, follow these steps:

#### 1.  Clone the repository:

```python
git clone https://github.com/OleksandrYanchuk/py-todo-list.git
```
#### 2. Open the folder:
```python
cd py-todo-list
```
#### 3. Create a virtual environment:
```python
python -m venv venv
```
#### 4. Activate the virtual environment:
   
##### - For Windows:
```python
venv\Scripts\activate
```
##### -	For macOS and Linux:
```python
source venv/bin/activate
```
#### 5. Install the project dependencies:
```python
pip install -r requirements.txt
```
#### 6. Apply database migrations:
```python
python manage.py migrate
```
#### 7. Start the development server:
```python
python manage.py runserver
```
#### 8. Open your web browser and go to http://localhost:8000 to access the application.

## Setting up Environment Variables

Todo project uses environment variables to store sensitive information and configuration settings. To set up the required environment variables, follow these steps:

#### 1. Rename a file name `.env_sample` to `.env` in the project root directory.

#### 2. Make sure to replace `your_secret_key_value_here` with your actual secret key.
