# py-todo-list

## Setup and Local Installation

### To set up and run the project locally, follow these steps:

#### 1.  Clone the repository:

```python
git clone https://github.com/OleksandrYanchuk/py-todo-list.git
```
#### 2. Create a virtual environment:
```python
python -m venv venv
```
#### 3. Activate the virtual environment:
   
##### - For Windows:
```python
venv\Scripts\activate
```
##### -	For macOS and Linux:
```python
source venv/bin/activate
```
#### 4. Install the project dependencies:
```python
pip install -r requirements.txt
```
#### 5. Apply database migrations:
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

## Use the following command to load prepared data from fixture to test and debug your code:
python manage.py loaddata todo_list_data.json

