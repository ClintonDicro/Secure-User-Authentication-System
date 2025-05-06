# Secure-User-Authentication-System

Task 1

A minimal FastAPI-based authentication system using JWT tokens and password hashing.


##Project Setup Instructions

### 1. Unzip and Navigate

- Unzip the provided project folder.
- Open a terminal (CMD or Terminal) inside the unzipped folder.


### 2. Set up Virtual Environment

### For **Windows**:
python -m venv myvenv
myvenv\Scripts\activate
pip install -r requirements.txt

### For macOS/Linux:
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt

3. Finally run the code using following command,
- uvicorn main:app --reload


API Testing with Postman

1. In that unzipped folder you can find Task_1.postman_collection.json, import the file in your postman

2. Inside Postman, look for the collection named Task_1.

3. You'll find three main requests: register, login and profile.

- register
    -Method : POST
    -url : http://127.0.0.1:8000/register
    -Body -> raw -> JSON
    -Example JSON data : {"username": "username", "password": "password"}
    -resister success you get following json,
    -{"message": "User register successfully"}

-login
    -Method : POST
    -url : http://127.0.0.1:8000/login
    -Body -> raw -> JSON
    -Example JSON data : {"username": "username", "password": "password"}
    -login success you get following json,
    -{
    "access_token": "<your_jwt_token_here>",
    "token_type": "bearer",
    "msg": "Login successfully"
    }

-profile
    -Method : GET
    -url : http://127.0.0.1:8000/profile
    -Authorization -> Auth Type -> select Bearer Token -> paste the token from login json
    -If success you get following json,
    {
    "msg": "Welcome username!"
    }

    
