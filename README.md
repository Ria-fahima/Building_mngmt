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
**Advantages of ORM**
* As ORM queries and manipulates data so no need to remember SQL commands.
* For creating a portable format, data serialization is necessary which is done by ORM.
<br>
## Documentation of all endpoints API
In the app, there are some API endpoints. Using those endpoints, certain operations can be done. 
For checking the authetication of a user, there are two endpoints.
<br>
* When a user wants to register to the app,
<br>
127.0.0.1:8080/auth/register
* When a user wants to login to the app,
<br>
127.0.0.1:8080/auth/login
<br>
## ERD of the Building App
<br>
![Screen Shot 2022-11-12 at 2 53 23 am](https://user-images.githubusercontent.com/105357829/201378873-adf6d1d9-027f-47c4-a69a-f7be8120c4df.png)









