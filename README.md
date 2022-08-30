# fastapi-crud
Implementation of CRUD functionality with FastAPI in python.

## main.py
Main application

## common.py
Some useful user-defined function.

## db.py
Contains a dictionary representing a database.

## templates
Contains HTML files.   
Render by Jinja2templates.

## static
Contains Image, CSS, JS files.

# Run
Install all required dependencies.
```
pip install fastapi
pip install uvicorn[standard]
pip install Jinja2
pip install python-multipart
```

Then run uvicorn from the command line.
```
uvicorn main:app --reload
```

# Others
If you have a lot of requests, using Pydantic library would be helpful.   
I don't use it in this project.   

