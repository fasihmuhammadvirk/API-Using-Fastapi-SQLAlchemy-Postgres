# About Repositories
In this i have created 5 Apis that do CRUD operation on the Database<br>
I have created the database using SQLalchemy<a href="https://github.com/fasihmuhammadvirk/SQLAlchemy">(About Sqlalchemy)</a>  and linked it with Postgressql<br>

# Notes 
Sort them using "Create Date 'OldestFirst' " 
<a href = "https://notebook.zoho.com/app/index.html#/shared/notebooks/r5oy285ca9198eb03402fa0358d13d68e2cd1/notecards" >Link to Notes</a>

# Setup
Follow these steps to setup this project/repository

  ### Open Your Project Directory
  The First setp is to open your Repository/Project Folder in Vs Code or any IDE.
  
  ### Install and Setup Virtual Enviornment.
  ##### 1. Install Virtual Enviornment
          pip3 install virtualenv
  ##### 2. Create a Virtual Enviornment
  ##### 2.1 Make sure you are in your project/repository folder
  ##### 2.2 Create a Virtual Environment
        virtualenv env
  ##### 3. Activate the Virtual Enviornment
  ##### For Macos
       source env/bin/activate
  ##### For Windows
       .\Scripts\bin\activate
       
  ### Download & Install Dependancies.
  #####  1. We need these for this Project pytest, sqlalchemy, fastapi, pydantic, uvicorn, coverage, pytest-cov
  #####  2. To install all these dependancies use this command
        pip3 pytest sqalchemy fastapi pydantic uvicorn coverage
  
  ### To run Server
  #####   1. I have created all the apis in main.py and also other concepts in different files 
  #####   2. To run Api server use this command
          uvicorn main:app --reload 
 # Test and Coverage.
  ### 1. To run Test 
       pytest test_main.py         
  ### 2. For Coverage 
       pytest --cov
  ### 3. For Coverage Report
       coverage report
     







