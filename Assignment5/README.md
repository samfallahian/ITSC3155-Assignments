### Installing necessary packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`  
### Import packages and make a fastapi Server:
`from typing import Union`  
`from fastapi import FastAPI`  
`app = FastAPI()`  
### Annotate functions with API URL
### Run the server:
`uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)