#!/usr/bin/env python3
# Script for an admin to add the users and also change their passwords
import pymysql as sql
import configparser
import getpass
import sys

def start_conn():
    conf = configparser.ConfigParser()
    conf.read_file(open('GFS.conf'))
    username = conf.get('database','user_name')
    passwd = conf.get('database','password')
    db = conf.get('database', 'db')
    host = conf.get('database', 'host')
    charset = conf.get('database','charset')
    conn = sql.connect(user=username, password=passwd,host=host,database=db,charset=charset)
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE()")
    data = cursor.fetchone()
    print(f"Connection established: {data}")
    return conn

def close_conn(conn_obj):
    conn_obj.close()

def create_new_user(conn):
    user_name = input("[!] Enter Username: ")
    pass1 = getpass.getpass()
    pass2 = getpass.getpass()
    if pass1 == pass2:
        hashed_pass = hash(pass1)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_info values(%s,%s)",(user_name, str(hashed_pass)))
        conn.commit()
    else:
        print("[-] Entered Passwords didn't match")
        return

def list_user(conn):
    cursor = conn.cursor()
    cursor.execute("select user_name from user_info")
    data = cursor.fetchall()
    print("[*] Usernames")
    index = 1
    for b in data:
        print(index,".",b[0])
        index = index+1

def delete_user(conn):
    user_name = input("[!] Enter the username to delete: ")
    cursor = conn.cursor()
    cursor.execute("delete from user_info where user_name = %s",(user_name))
    conn.commit()

def main():
    conn = start_conn()
    while True:    
        var = """Select Function:
        1.  Create new user
        2.  List users
        3.  Delete user 
        4.  Exit
        """
        print(var)
        sw = input("Enter Input: ")
        if int(sw) == 1:
            create_new_user(conn)
        if int(sw) == 2:
            list_user(conn)
        if int(sw) == 3:
            delete_user(conn)
        if int(sw) == 4:
            conn.close()
            sys.exit(0)

if __name__ == "__main__":
    main()