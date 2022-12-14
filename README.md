# Building_Management_App
## Github Repo
[Building Management App](https://github.com/Ria-fahima/Building_mngmt)
<br>
## Problem Identification
Nowadays, in many buildings the apartments are being sold to the customer.The residents need to know all information related to the building. There can be some annoucements, meetings which need to be known to the residents. 
<br>
There can be a situation where the residents can leave the apartment. So, this records must be recorded somewhere.
<br>
All the necessary information of a resident need to be updated by the building manager.
Again, the residents can have some trouble in the building. As here residents live in the apartments they can be either tenant or owner. If they face any issue or something then they need to have the oppurtunity to complain about it.
<br>
The staff recruiment process, their role and accessibility etc need to be stored somewhere for the personal identification.
## Reason to solve the problem
This kind of problems can cause trouble both for residents and staffs in the building. The building manager can send email to individual resident but it is a ineffective process as it kills a lot of time. Again, an app can solve many problem. All the residents just can go to the link to know the recent annoucements/meetings. Also, users(both residents and staffs can complain about anything which can be inappropriate for him/her). This complain list can also be seen through a link.
<br>
The building manager(who is admin of the app) can delete or update any information(e.g: car number, fob number etc) of a resident at any time. As fob can be broken so a new fob maybe replaced the old one. 
<br>
Again, an admin of the app can add resident to the resident list and can delete the full details if the resident leave the apartment.
<br>
The admin can also add, delete or update any information of a staff from the user of the building app.
<br> 
A user can complain in this app which is convenient to the user.
## Database System
For the building management app, i have chosen **PostgreSQL Database System**. As it is a open source DBMS, it has a wide range of possibilities for further developement. Also a large number of communities use this. Modules can be developed by the users and it can be propsed to the community later. It can handle large quantity of data without crashing. In postgreSQL bugs can be identified easity so that it is easy to improve and upgrade. This system is also compatible with different types of data. For data serialization, ORM plays an important role. In PostgreSQL, a user does not need to learn ORM seperately to serialize the data. That's a huge benefit of using PostgreSQL. Again,Low maintenance and administration for both embedded and enterprise use of PostgreSQL.
<br>
**Drawbacks of PostgreSQL** : PostgreSql does not own by one organisation. As it focuses on compatibility, for speed requirement if any change happens, then it needs more work than MySQL. Some open source apps do not support PostgreSQL. If it is rated for performance, then it is slower than MYSQL.
<br>
## Benefits of ORM
ORM(Object Relational Mapping) is a layer between the relational database and the programming language. It lets the user to query and manipulate data without using the sql commands in the code. A developer can write the code in his preferred language without SQL statements. 
<br>
**Functionalities of ORM**
* It connects to the database server.
* It generates Query.
* It sanitize the parameters if it is needed.
* It fetches data and serialize it.
* It secures the query.
<br>
<br>
**Advantages of ORM**
<br>
As ORM queries and manipulates data so no need to remember SQL commands. For creating a portable format, data serialization is necessary which is done by ORM.
<br>
## Documentation of all endpoints API
<br>
In the app, there are some API endpoints. Using those endpoints, certain operations can be done. 
For checking the authetication of a user, there are two endpoints.
<br>
* When a user wants to register to the app,
<br>
127.0.0.1:8080/auth/register
<br>
<br>
* When a user wants to login to the app,
<br>
127.0.0.1:8080/auth/login
<br>
<br>
<br>
All the users can see the user table in the database so that they can have the idea of the existing database.
<br>
To get all users,
<br>
127.0.0.1:8080/users
<br>
<br>
To get the certain user information by using the id. To get only one user at a time with the id,
<br>
127.0.0.1:8080/users/id   ; here id = 1/2/3 etc and it is the user_id
<br>
<br>
To have the information about the existing residents, the below API will work.
<br>
127.0.0.1:8080/users/residents
<br>
<br>
To get only one resident information, his/her id will be needed here.
<br>
127.0.0.1:8080/users/residents/id   ; here id is the resident_id
<br>
<br>
A building Manager who is the admin of this app can add a resident from the existing user table. For that reason, with certain information of the residents and the user_id of the resident is needed.
<br>
127.0.0.1:8080/users/residents/id   ; Here the method will be **post** and id is the **user_id** and the authorization is required.
<br>
<br>
If a resident leave the apartment, then all information will be deleted by the Manager.
<br>
127.0.0.1:8080/users/residents/id  ;  Here the method will be **delete** and id is the **resident_id** and the authorization is required.
<br>
<br>
For updating any information of a resident,
<br>
127.0.0.1:8080/users/residents/id  ; Here the method will be **put/patch** and id is the **resident_id** and the authorization is required.
<br>
<br>
<br>
To have the information about the existing staffs, the below API will work.
<br>
127.0.0.1:8080/users/staffs
<br>
<br>
To get only one staff information, his/her id will be needed here.
<br>
127.0.0.1:8080/users/staffs/id   ; here id is the staff_id
<br>
<br>
A building Manager who is the admin of this app can add a resident from the existing user table. For that reason, with certain information of the residents and the user_id of the resident is needed.
<br>
127.0.0.1:8080/users/staffs/id   ; Here the method will be **post** and id is the **user_id** and the authorization is required.
<br>
<br>
If a staff leave his/her job, then all information will be deleted by the Manager.
<br>
127.0.0.1:8080/users/staffs/id  ;  Here the method will be **delete** and id is the **staff_id** and the authorization is required.
<br>
<br>
For updating any information of a staff,
<br>
127.0.0.1:8080/users/staffs/id  ; Here the method will be **put/patch** and id is the **staff_id** and the authorization is required.
<br>
<br>
The users can complain if anything happens. To get all complains,
<br>
127.0.0.1:8080/complains 
<br>
<br>
To get a specific complain with complain_id,
<br>
127.0.0.1:8080/complains/id   ; here id = complain_id
<br>
<br>
If a user wants to post a complain then,
<br>
127.0.0.1:8080/complains  ; Here the method is **post**
<br>
<br>
A user can delete any complain_id if it's needed.
<br>
127.0.0.1:8080/complains/id  ; Here the method is **delete** and id will be **complain_id**
<br>
<br>
If a user wants to updte something in the message of the complain section, it is allowed to do. 
<br>
127.0.0.1:8080/complains/id  ; Here the method is **put/patch** and id will be **complain_id**
<br>
<br>
<br>
The user needs to know all upcoming annoucements/meetings. 
<br>
127.0.0.1:8080/annoucements  
<br> 
<br>
To get the specific annoucement with annoucement_id,
<br>
127.0.0.1:8080/annoucements/id  ; here id = annoucement_id
<br>
<br>
If the Manager wants to post an annoucement/ meeting, then the below API will be needed.
<br>
127.0.0.1:8080/annoucements  ; Here method will be **Post** and authorization is needed.
<br>
<br>
Sometimes meeting/annoucements can be cancelled. So to delete the annoucement,
<br>
127.0.0.1:8080/annoucements/id  ;  Here method will be **delete** and authorization is needed and id = annoucement_id.
<br>
<br>
To update any information of the annoucement, An admin(Building Manager) need to apply the below API endpoint,
<br>
127.0.0.1:8080/annoucements/id ;  Here method will be **put/patch** and authorization is needed and id = annoucement_id.
<br>
<br>
Any user can comment in the annoucement. To post the comment the below endpoint will work.
<br>
127.0.0.1:8080/annoucements/id/comments   ;  Here method will be **post**  and id = annoucement_id.


## ERD of the Building App
![Screen Shot 2022-11-12 at 2 53 23 am](https://user-images.githubusercontent.com/105357829/201440679-33aaeea6-928a-436f-b0ed-ee3940cb6729.png)

<br>

## PYPI Packages
In my app, i have used some PYPI packages which are not built-in. 
1. Flask pip: This pip is installed to run and function the flask app that is created. It is a Web application framework. It has the ability to build up a complex app.
2. flask-marshmallow: This pip package does the ORM function. So data is sanitized and serialized. It is a thin integration layer for flask and marshmallow. It is object relational mapping library that can convert object from the python code and vise versa.
3. flask-jwt-extended : To create the JWT token and have the identity from the token some functions are used. Those functions are included in flask-jwt-extended pip package. For security purposes and for authentication, JWT is necessary. For some functions in the app which can only be done by the authorised person, get_jwt_identity is used, which is imported from this pip package.
4. flask-SQLAlchemy : This pip pacakge helps to create the SQL tables in the programming language. Without using the regular format to make an SQL table, this package creates a model for the variables. It is a toolkit that gives efficient and high performing database by accesing the relational databses.
5. psycopg2: THis one is the databse adapter. To complete implementation in python and to perform the thread safety this package works a lot. To perform PostgreSQL operations using python language, this databse driver is used.
6. python-dotenv : This package reades the key value from the dot file. In my code, there are two dot files(.env, .flaskenv). This structure is usually used in developement process. It reads the key value from the .env file as put those values in the environment variable.
7. flask-bcrypt : For security purposes, password and other informative and sensitive data need to be secured. For this reason, flask-bcrypt is used. By applying the hashing method to the password, this process is done. So that it is quite impossible to get the password to hack the data. It gives the bcrypt hashing facilities for the app.

## Project Model and Relationship of the elements in the Model
### User Model
![Screen Shot 2022-11-12 at 10 37 35 am](https://user-images.githubusercontent.com/105357829/201444588-6a151b01-8f72-40ba-a4b6-f40987f101b0.png)
<br>
<br>
In the User Model, all the information of the registered users can be achieved. The tablename for the User Model has been set as users. There is a id for th user which is unique for the users table. This is why it is the primary key and data type of id is integer. Then f_name(first_name) is a column of the table which is a string data type and can not be null while registering as a user. Next, l_name(last name) has the same properties like f_name. There is a column in the users table which is email, It is a string data type, can not be null and must be unique from other users. 
<br>
<br>
**Relationship with the User Model**
The User Model has the relationship with the Comment Model. In theUser Model, the parent and child model relationship has been established where a user can make multiple comments.Again, similarly a resident and a user has a relationship between them. Also, a user can be a staff in this app so that there is a relationship between these Models as well. Finally, a user can complain so that there is a relation between them.
<br>
<br>
### Staff Model
![Screen Shot 2022-11-12 at 11 15 12 am](https://user-images.githubusercontent.com/105357829/201446691-02ed081b-4e14-4f57-bbae-7bd030144fc1.png)
<br>
<br>
In the Staff Model, There is a table called staffs. Also in the table, for each staff a unique id is created whose data type is integer and which is a primary key. There is a string data type which is named as role to categorized the position of the staff. Also, for many functions, the authority is given only to the admin so that is_admin is another column which has been created. This is_admin data type is boolean and it's default value is false. In the Staff Model, a foreign key has been used which is the user_id. This can not be null and it's data type is integer. 
<br>
<br>
**Relationship with the Staff Model**
In the Staff Model, there are few realtionships. The Staff Model is firstly related to the User Model. Again, The staff model has a relationship with the Annoucement Model so that an authorized staff can call/create many annoucements. Again, as the authorized staff can add resident from the user so that there is a relationship between the Staff model and the Resident Model.
<br>
<br>
### Resident Model
![Screen Shot 2022-11-12 at 11 28 12 am](https://user-images.githubusercontent.com/105357829/201447420-5721be16-1dde-4f4d-8779-1a2ade765b8f.png)
<br>
<br>
In the Resident Model, a table is created named residents. There is a id which data type is integer and it is the the primary key of the table. A fob column has been established where the fob number is stored for the resident. Initially, it can be empty. This fob_num datatype is integer. There is a column for the car number which is named as car_num. This element's datatype is string. There is a unit column where the unit of the residents need to be stored.This unit datatype is integer and it can not be null. Again,there is another column is_owner which is false by default and it's datatype is booolean. There are two foreign keys which has been used. One is the user_id, this one demonstrates that the resident is a user before. This foreign key data type is integer and can not be null. On the other hand, there is another foreign key which is staff_id, this one is also integer and it can not be null as well. As an authorized staff can add a user to the resident database that is why this staff_id is also needed.
<br>
<br>
**Relationship with the Resident Model**
In the Resident Model, there are two relationship with this. One is with the User Model and it has also cascade delete so that when the resident will leave the apartment , the user will be automatically deleted. Another relationship is between the Staff Model and Resident Model.
<br>
<br>
### Annoucement Model
![Screen Shot 2022-11-12 at 11 44 50 am](https://user-images.githubusercontent.com/105357829/201448254-4b7faaeb-f31a-4369-bcbf-6e0eccecd792.png)
<br>
<br>
In the annoucement Model, there is a primary key which unique and is named as id. Again, the data type is integer. There is subject column which can not be nullable and datta type is string. Here the annoucement subject will be stored. Next, there is a column called message, it is a text data type and can not be null. There is a date column where the date of the annoucement will be stored. The data type of date is also date so that it can take the current date while making an annoucement in the app. There is a foreign key which is a integer that is staff_id and it can not be nullable.
<br>
<br>
**Relationship with the Annoucement Model**
In the Annoucement Model, there is a relationship between the STaff Model and the Annucement Model. As an authorized staff can make one or many annoucements. Again, there is a relationship between the Comment Model and the Annoucement Model as in the annoucement segment multiple comments can be existed.
<br>
<br>
### Comment Model
![Screen Shot 2022-11-12 at 11 56 00 am](https://user-images.githubusercontent.com/105357829/201448778-8f9f5d41-7792-4c5a-85d9-a1019551bc56.png)
<br>
<br>
In the Comment Model, there will be an integer type id which will be the primary key. then there is a message column which data type is text. Again, there is a date column, which will store the date when the comment will be created in the database. The data type of date is date. There are two foreign keys. One is user_id another one is annoucement_id.
<br>
<br>
**Relationship with the Comment Model**
There are mainly two relationship in the Comment Model. One relationship is with the User Model as a user can comment in the Comment Model and another relationship is with the Anooucement Model as in one annoucement there can be many comments.
<br>
<br>
### Complain Model
![Screen Shot 2022-11-12 at 12 02 57 pm](https://user-images.githubusercontent.com/105357829/201449122-a2e329e6-7e30-4b9c-9176-149682a680f9.png)
<br>
<br>
In the Complain Model, There is a primary key id which is a integer. A date column is created where the complain date will be stored and the data type of the column is date. Next, there is a unit column which is integer as well. The title of the complain is stored in the title column and which data type is string. There is a message column where the complain is written with a brief explanation. In the Complain Model, there is also a foreign key user_id. This user_id data type is integer and it can not be null.
<br>
<br>
**Relationship with the Complain Model**
In the complain model, there is only one relationship with the user as users can complain and have the accessibility to do this.
<br>
<br>
## Database Relationships in the application
In the application, there are many relationships that have beeen implemented in the database. In the ERD model the relationship can be identified easily.
<br>
<img width="465" alt="Screen Shot 2022-11-12 at 1 45 46 pm" src="https://user-images.githubusercontent.com/105357829/201453070-1021cb54-bc55-40bd-86e6-13e9f02a9c3f.png">
<br>
In the ErD model, the users table and the staffs table are related. After registering and putting details in the login information a user is exist in the users table. but later an authorised staff from the staffs table(who is the admin) can add staff from the new users. Also, The users table and the staffs table has the one-to-one connection. That means a user can be one and only staff in the staffs table if the criteria matches. In the Staffs table, the user id is the foreign key which denotes that the person is a user of this app. But the authorized admin wants to create a seperate table for staffs so that the staff id is unique for the person.
<br>
Again, in the ERD Model, it is clearly visible that in the Users table and the complains table there is a one-to-many relationship. So, a user(either resident or a staff) can write many complains. Same for the relation between Users table and Comments table. A user can comment as many as he/she wants. In the comments table, user_id is considered as the foreign key as it comes from the users table whereas comment id is the primary key which is unique and each comment can be found by providing the unique id of the comments.
<br>
<img width="452" alt="Screen Shot 2022-11-12 at 1 54 52 pm" src="https://user-images.githubusercontent.com/105357829/201453321-b87ff7db-ca86-4ac0-a2de-9c1f7fb5bd8f.png">
<br>
In the Users table and the residents table, there is a relation between them which is one-to-one relationship. A user can be one and only resident in the app. 
<br>
All these relationships are connected with each other through the primary key and the foreign key. One table's primary key sometimes work as a foreign key for another table. Suppose in the resident table, The resident id is unique for the residents but there is also an id which is user id that comes from the Users table. Here, the user id is the foreign key.
<br>
For adding the resident to the residents table, an authorised admin (who is also a staff) can add. So here is a relationship between the residents table and staffs table and that is one-to-many relationship.
<br>
<img width="720" alt="Screen Shot 2022-11-12 at 1 59 22 pm" src="https://user-images.githubusercontent.com/105357829/201453473-a18c72d6-6681-44de-b031-131ff9619b11.png">
<br>
So, an authorized staff can add residents as many as he/she wants to.
<br>
There is a relation between the staff table and the annoucements table. This one is one-to-many relationship as an authorised admin or staff can make more than one annoucements. In the annoucements table, staff_id is the foreign key as this directly related to the staffs table. In the coding, there is a condition of authorization of the staff who is admin can control the annoucement process.
<br>
<img width="455" alt="Screen Shot 2022-11-12 at 2 03 19 pm" src="https://user-images.githubusercontent.com/105357829/201453624-62dfa6e6-325d-44aa-872d-aabfe046297d.png">
<br>
Again, there is a relationship betweeen annoucements and comments table. This relationship is one-to-many. As in the annoucements table there can be one or more comments that has been done by the users.
<br>
<br>
## Project Management Process
In the app, there are some steps exist that need to be done before working with the code in a perfect manner. In the gitignore file, it is clearly shown that three items are included there so that those things won't be present in the repo. 
* .venv : .venv is the virtual environment that is excluded in the repo as it really does not make any difference. If a developer works in the virtual environment then if he/she provides his/her code to others then the situation is something like this- "If the recepient does not have the virtual environment, then maybe he/she needs to create one. In the terminal one needs to write the following code - **python3 -m venv .venv**. After creating the environment, he/she needs to activate it with this command in the terminal - **source .venv/bin/activate**, then the virtual environment will be activated.
* .env : For the security purposes, the file is not included to the repo. But to give an outline that what type of information were in the actual .env file, a sample file of .env is created. In the .env_sample file, the information is not given directly for security reason but some hints are provided so that the developer can guess.
But for functioning the code properly, the hidden things are revealed below-
* **Database URL** : DATABASE_URL = postgresql+psycopg2://rockwall_user:rockpass123@127.0.0.1:5432/rockwall_apt
<br>
Here, rockwall_apt is the database that needs to be created in the recepient PostgreSQL with the command **create database rockwall_apt** .
<br>
Again, here **rockwall_user** is the user who get the access for the certain database and the password for the user should be set as **rockpass123**. 
<br>
After setting up these things, the programming language will be connected to the SQL commands. 
<br>
* **JWT SECRET KEY** : JWT_SECRET_KEY = 'hello rockstars'
<br> 
It is a secret key for the JSON Web Token. For security reasons of an app, this information is hidden deliberately. 
<br>
Another file which is .flaskenv is hidden for confedentiality purposes.
The values are given below - 
<br>
.flaskenv
<br>
FLASK_APP = main
<br>
FLASK_DEBUG =1 
<br>
FLASK_RUN_PORT = 8080
<br>
### 5 steps for Project Mnagement Process:
There are mainly 5 phases to complete an entire project management system. Those steps are given below-
<br>
<br>
* Project Initiation : At first, an idea should come up to solve a problem. The main concern is what benefits can be achieved by solving the problem, what are the main goals etc. In my app, some problems have been identified in the building management system that need to be solved. The main goals to build up this app are the users can make complains if they needed, all information about the residents and staffs will be stored. if there is any annoucement, the users can know about it and comment their opinion. 
<br>
<br>
* Project Planning: In this process, a planning is done so that it is easy to proceed. This determines that how the things should go, what steps should be taken to build the app with proper guidance. In this phase, how many models should be created and what will be the connection among those models are determined. Also, the number of controllers and routes are assumed in this planning phase. This phase is very crucial. Before implementing the code, a proper planning is needed for efficiency. If the planning works out properly then the path is comparatively easy to code.
<br>
Also in this phase, the ERD and modling are created to establish what the outcome will be by implementing those relationships among those tables. Again, database create and it's granted user and required password are done in this phase.
<br>
<br>
* Code Implementation and Project Execution: After coding the app, in this phase the result is executed. This phase is the most important part as it relates to the code which is the main factor for the project. While coding the app, DRY principles and other requirements are considered so that the code is effective. All the functions, schemas, controllers, routes etc are structured in this way so that it worked properly. 
<br>
In this phase, models are created to connect with SQL language. Controllers are created to control the models with certain commands. Routes are defined to get the certain output with the unique endpoint API. For analysing whether the code works properly or not, the localhost is connected to the postman. There with all endpoints API we can check whether the desire value comes or not. Flask association are also done in this phase. All the models are connected with each other by foreign key.
<br>
There are certain things that can only be done by an authorised person. Those function are also implemented.
<br>
<br>
* Monitoring & Controlling: After execution, the code need to be kept under monitoring. If any routes or function or anything is not working according to the code, then the problem should be found out and take the further process to solve this. Everytime in the testing process, a lot of bugs come out and then developers handle those bugs precisely. This phase really improves coding and make it more professional.
<br>
After analysing and monitoring the results from postman, there were certain error comes up that need to be solved. Such as KEYERROR, VALIDATION ERROR, 404,401 etc. if a user mistakenly puts a n input that can bring up false value or error then it need to taken care of. In this phase all those errors are handled properly. Again, there are some validation implemented to the code to make the code more secure like in password Regex function is implemented.
<br>
<br>
* Project Closing: After all of the above steps, the project can be considered to it's final position where the developer get the output exactly what he/she wants. Also, if there is any kind of misleading value, the final phase of an app should handle those.

















