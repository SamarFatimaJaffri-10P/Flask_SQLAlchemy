# Flask_SQLAlchemy
Learning SQLAlchemy with Flask and PostreSQL

## Connect to Database
For conneting to database you first have to create a database.

### Create Database
- Write command `psql` for going into psql shell
- Once into shell run the following
  ```
  # create database database_name;
  create database flask_sqlalchemy;   # where flask_sqlalchemy is my database name
  ```
  Don't forget the **;** at the end else the command will wait for line terminator to run.
- Type `\q` to exit the shell

### Create Tables
After creating database, create tables.
- Write command `flask shell` to start the flask shell
- Once into shell run the following
  ```
  from app import db
  db.create_all()
  exit()
  ```
  In the first line db is imported from app (db is the object of SQLAlchemy), second line call a function `create_all()` which create all the Models (tables) in the database, third line exit the flask shell.

### Connect to Database
Now for connecting to database goto psql shell again by using command `psql`
- Once into shell run the following for onnecting to database
  ```
  # For connecting to database, \c database_name
  \c flask_sqlalchemy
  ```
- Run the following for displaying the list of relations
  ```
  # For displaying list of relations
  \d
  ```
- Run the following for displaying list of tables
  ```
  # For displaying list of tables
  \dt
  ```
- Run the following for displaying a particular tables
  ```
  # For displaying a particular table, \d table_name
  \d product
  \d order
  \d customer
  ```

<details>
<summary> Course link </summary>

### Course link
[Flask-SQLAlchemy Basics](https://courses.prettyprinted.com/courses/enrolled/1016334)
</details>
