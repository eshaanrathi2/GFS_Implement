import getpass
import pymysql as sql
import configparser
import hashlib
import sys

def start_conn():
    conf = configparser.ConfigParser()
    conf.read_file(open('GFS.conf'))
    username = conf.get('database','user_name')
    passwd = conf.get('database','password')
    db = conf.get('database', 'db')
    host = conf.get('database', 'host')
    charset = conf.get('database','charset')
    try:
        conn = sql.connect(user=username, password=passwd,host=host,database=db,charset=charset)
    except:
        print("[-] MySQL Server is currently not running...")
        sys.exit(0)
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE()")
    data = cursor.fetchone()
    print(f"Connection established: {data}")
    return conn

def authenticate_user():
    user_name = input("[!] Enter Username: ")
    password = getpass.getpass()
    hashed_pass = hashlib.md5(password.encode())
    conn = start_conn()
    cursor = conn.cursor()
    cursor.execute("select hashed_pass from user_info where user_name like %s",(user_name))
    try:
        pass_from_db = cursor.fetchone()[0]
    except:
        print("[-] Invalid Username")
        return -1
    if hashed_pass.hexdigest() == pass_from_db:
        print("[+] Authenticated")
        return 1
    else:
        print("[-] Passwords didn't match")
        return -1
