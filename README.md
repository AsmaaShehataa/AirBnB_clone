# Welcom to the Airbnb Clone Project Folder
<img src="https://user-images.githubusercontent.com/69850751/175876062-f252cc1b-bd44-46b3-9ddb-a7692b2eede4.png" alt="this is the holbertoon school / alx logo" />



## Language
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- Name of the project : ``0x00 AirBnB clone - The console``
- Authors : <br>
[Mohamed Amouch](https://github.com/amch-med23) <br>
[Asmaa Shehata](https://github.com/AsmaaShehataa)


### Overview:
AirBnb clone Project is so useful for the developers to start working on it as there are a lot of concepts to digest and understand as a practical work -- and here are we had worked on: 

Creating Classes and Models:
This is done to handle the logic that defines the interprocess comunications betwen deferant parts of the project.

Creating the console application: 
was ultimatly created to get the idea of how backend data is beign handled at the user side,<br> rhis was crated by using the cmd module <br>

CRUD Operations are supported - (Create -Read -Update - Delete)<br>

where a user can create, update, show / list (read) or even destroy any object with its ID and a class name.<br>

how to start it:
-------------------

we start the console by excuting this command:<br>
1- python3 console.py <br>
2- (HBNB) --&gt; start using any of the CRUD operations, (whether if the user needs to create, show, update or delete Objects) <br>

How to use it: 
--------------------

in Interactive mode: <br>

$ ./console.py <br>
(hbnb) help <br>

 ``Documented commands (type help ``&lt;``topic``&gt;``):`` <br>
 ``-------------------------------------------------`` <br>
 ``EOF   help   all   destroy   show   create   update   quit`` <br>

(hbnb) <br>
(hbnb) <br>
(hbnb) quit <br>
$ <br>


non-interactive mode:<br>

$ echo "help" | ./console.py <br>
(hbnb) <br>

 ``Documented commands (type help ``&lt;``topic``&gt;``):`` <br>
 ``---------------------------------------`` <br>
 ``EOF   help   all   destroy   show   create   update   quit`` <br>
(hbnb) <br>
$ <br>
$ cat test_help <br>
help <br>
$ <br>
$ cat test_help | ./console.py <br>
(hbnb) <br>

 ``Documented commands (type help ``&lt;``topic``&gt;``):`` <br>
 ``--------------------------------------- ``<br>
 ``EOF   help   all   destroy   show   create   update   quit ``<br>
(hbnb) <br>
$ <br>


examples
---------

**Creating an Object based on a class name** <br>

create &lt;class name&gt; <br> ``Ex: create BaseModel`` <br>

-> this will output the id of the created object.<br>
 
**Showing an Object** <br> 

show &lt;class name&gt; &lt;object id&gt; <br> ``Ex: show User it's_id ``

--> this will show the string representation of the object you specified

**Updating an Object** <br>

update &lt;class name&gt; &lt;object id&gt; &lt;attribute name&gt; &lt;value&gt; <br> ``Ex: update User it'_id name Asmaa``

-> this will update the specified attribute value to Mohamed in the specified instance

**Destroying an Object** <br>

-> this will destroy the specified object

destroy &lt;class name&gt; &lt;object id&gt; <br> ``Ex: destroy User it's_id``
