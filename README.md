# Instagram Clone 

## Author
 [Alvynah Wabwoba](https://github.com/alvynah)


# Description
This is a Django web application.It is a simple Expense Tracker that illustrates CRDUD functionalities .




## Live Link

[transactiont](https://transactiont.herokuapp.com/)

## User Story

1. View posted expenses and their details.
2. Post an expense.
3. Edit an expense.
4. Delete an expense.
3. Search for an expense 
6. View my profile page


## Behaviour Driven Development (BDD)

1. Sign up to the application

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on sign up  | username,password,email | user account and profile is created  | 

2. log into the application 

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Enter details in the log in form   | username, password| Landing page is loaded is login is successful else an error message is shown  | 


|  

3. Post Transaction

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on tab  expense on the navbar, and click add transaction button | Enter required details| Transaction is posted and displayed on the page | 



## Bugs
### Currency
1. Only works with Kenyan shillings



## Setup/Installation Requirements
### Getting the code
1. clone repository
   https://github.com/alvynah/Expense_Tracker.git
    
2. Move to the folder and install requirements
    cd Expense-Tracker
    pip install -r requirements.txt
### Database

1. Set up Database,and put your username and password in the code

2. Make migrations
    python3 manage.py makemigrations picture

3. Migrate
   python3 manage.py migrate 
    
### Running the Application
1. Run main apllication
   * python3 manage.py runserver

2. Run tests
    
   * python3.6 manage.py test picture

## Technologies Used

* Python3.6
* Django 3.2
* Bootstrap
* PostgreSQL
* CSS
* Heroku

## Contact Information
For any further inquiries or contributions or comments, reach me at [Alvynah](juvatalvynah@gmail.com)
### License
[MIT License](https://github.com/alvynah/Expense_Tracker/blob/master/License)

Copyright (c) 2022 **Alvynah Wabwoba**
