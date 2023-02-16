**0x0D. SQL - Introduction**

**General**
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

**More Info**

*Comments for your SQL file:*

*cat my_script.sql*

*-- 3 first students in the Batch ID=3*

*-- because Batch 3 is the best!*

*SELECT id, name FROM students WHERE*
 *batch_id = 3 ORDER BY created_at DESC LIMIT 3;*

**Install MySQL 8.0 on Ubuntu 20.04 LTS**

*sudo apt update*

*sudo apt install mysql-server*

*mysql --version*

*mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))*


**Connect to your MySQL server:**

*sudo mysql*