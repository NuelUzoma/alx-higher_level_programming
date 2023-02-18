**0x0E. SQL - More queries**

**General**
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

**More Info**

**Comments for your SQL file:**

*cat my_script.sql*

*-- 3 first students in the Batch ID=3*

*-- because Batch 3 is the best!*

*SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;*

**How to import a SQL dump**

*echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p*

*Enter password:*

*curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows*

*Enter password:*

*echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows*

*Enter password:*

id  name

1   Drama

2   Mystery

3   Adventure

4   Fantasy

5   Comedy

6   Crime

7   Suspense

8   Thriller