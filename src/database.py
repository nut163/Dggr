```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        return conn
    except Error as e:
        print(e)

def close_connection(conn):
    conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_user(conn, user):
    sql = ''' INSERT INTO users(user_id,username,password,email)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    return cur.lastrowid

def create_dog_profile(conn, dog_profile):
    sql = ''' INSERT INTO dog_profiles(dog_id,name,breed,age,gender,description)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, dog_profile)
    return cur.lastrowid

def create_match(conn, match):
    sql = ''' INSERT INTO matches(match_id,user_id,dog_id,matched_user_id,matched_dog_id)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, match)
    return cur.lastrowid

def create_chat(conn, chat):
    sql = ''' INSERT INTO chats(chat_id,user_id,dog_id,matched_user_id,matched_dog_id,message)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, chat)
    return cur.lastrowid

def create_subscription(conn, subscription):
    sql = ''' INSERT INTO subscriptions(subscription_id,user_id,plan,price,start_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, subscription)
    return cur.lastrowid

def create_advertisement(conn, advertisement):
    sql = ''' INSERT INTO advertisements(ad_id,advertiser,content,clicks)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, advertisement)
    return cur.lastrowid

def create_location(conn, location):
    sql = ''' INSERT INTO locations(location_id,user_id,longitude,latitude)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, location)
    return cur.lastrowid
```