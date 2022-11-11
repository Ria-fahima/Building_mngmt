# Building_Management_App
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
<br>
The ERD image is given below-
<br>
![Screen Shot 2022-11-12 at 2 53 23 am](https://user-images.githubusercontent.com/105357829/201440679-33aaeea6-928a-436f-b0ed-ee3940cb6729.png)

<br>

## PYPI Packages
In my app, i have used some PYPI packages which are not built-in. 
1. Flask pip: This pip is installed to run and function the flask app that is created.
2. flask-marshmallow: This pip package does the ORM function. So data is sanitized and serialized.
3. flask-jwt-extended : To create the JWT token and have the identity from the token some functions are used. Those functions are included in flask-jwt-extended pip package.
4. flask-SQLAlchemy : This pip pacakge helps to create the SQL tables in the programming language. Without using the regular format to make an SQL table, this package creates a model for the variables.
5. psycopg2: THis one is the databse adapter. To complete implementation in python and to perform the thread safety this package works a lot.
6. python-dotenv : This package reades the key value from the dot file. In my code, there are two dot files(.env, .flaskenv). This structure is usually used in developement process.
7. flask-bcrypt : For security purposes, password and other informative and sensitive data need to be secured. For this reason, flask-bcrypt is used. By applying the hashing method to the password, this process is done. So that it is quite impossible to get the password to hack the data.










