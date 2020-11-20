# Google File System

Implementation with Python 3. [**Implemented using this GitHub repo**](https://github.com/Bereket-G/Google-File-System-Implementation-with-Python). Added features:
* Authentication of Username and Password. Username and password stored in MySQL server, and password stored using MD5 encryption.
* Added file [admin.py](https://github.com/rhitayu2/GFS_Implement/blob/main/admin.py) for adding, creating and listing users.
* Ported to Python3
 ***

## Table of Contents
1. [Set Up](#set-up)
2. [Running](#running)
3. [Extras](#note)

## Set Up

* **Setting up Database:**
    * Set up a MySQL `<user_name>` and `<password>`.
    * Create a database in MySQL. `create database <db_name>`
    * Import the database file in the repository.  `mysql -u <username> -p <db_name> <  dump_file.sql `.

* **Installing Requirements**
    * `pip3 install -r requirements.txt`

## Running

* **Admin Functions**
    * `python3 admin.py` to add, delete or list users

* **Running sequence of Servers**
  * The sequence for running the servers are as follows: Primary Backup Server --> Master Server --> Chunks Server
  * `python3 primary_BackUp_Server.py`
  * `python3 Master_Server.py`
  * `python3 Chunks.py`

* **Running Client**
    * The Client Node would be able to perform the functions of: download (get), upload (put), remove (delete) and list the current files in the cloud server
    * *Upload* : `python3 Client.py put <destination_file> <src_file>`
    * *Download* : `python3 Client.py get <destination_file>`. This will give the output of the data stored in the file. To store it in our local directory, pipe it into another file:
    `python3 Client.py get <destination_file> | tee src_file`
    * *Delete* : `python3 Client.py <destination_file>`
    * *List* : `python3 Client.py list`

## Note
* The directory for the Google Filesystem would be `~/` of each chunk server.
* Each of the 4 operation would require the authentication of user.
* The database and chunk size can be defined in the GFS.conf
