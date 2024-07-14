import sqlite3 as sq
import os
import random

with open(".//files/default.jpg","rb") as f:
    ava=f.read()


class SQL:
    
    def __init__(self,db):
        self.connect=sq.connect(f"./src/db/{db}.db")
        self.cursor=self.connect.cursor()
        self.Table_user='''CREATE TABLE User_data(
            ID_usr TEXT PRIMARY KEY,
            Login TEXT NOT NULL,
            Name TEXT NOT NULL,
            Surname TEXT NOT NULL,
            Password TEXT NOT NULL,
            Avatar BLOB DEFAULT NULL
            );'''
        self.Table_user_info='''CREATE TABLE User_info(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Birhtday TEXT DEFAULT '00.00.0000',
            City_birthday TEXT DEFAULT 'City',
            City_live TEXT DEFAULT 'City',
            Email TEXT DEFAULT '-',
            Nomber TEXT DEFAULT '-',
            ID_usr TEXT NOT NULL,
            FOREIGN KEY (ID_usr) REFERENCES User_data(ID_usr)
            );'''
        self.init_()
        self.init__()
        
    def init_(self):
        self.PhotoChange='UPDATE User_data SET Avatar = ? Where Login = ?'
        self.Select='SELECT * FROM User_data WHERE Login=? AND Password=?'
        self.Select_all='SELECT ID_usr,Name,Surname,Avatar FROM User_data WHERE ID_usr=?'
        self.Select_such="SELECT ID_usr,Name,Surname,Avatar FROM User_data WHERE Name LIKE ?"
        self.Select_all2='SELECT ID_usr,Name,Surname,Avatar FROM User_data'
        self.Select_login='SELECT * FROM User_data WHERE Login=?'
        self.Select_name='SELECT Name FROM User_data WHERE ID_usr=?'
        self.Select_id='SELECT ID_usr FROM User_data WHERE Login=?'
        self.Select_ava='SELECT Avatar FROM User_data WHERE ID_usr=?'
        self.INSERT='INSERT INTO User_data (ID_usr,Login,Name,Surname,Password,Avatar) VALUES (?,?,?,?,?,?)'
        self.Select_info='SELECT Name,Surname,Avatar FROM User_data WHERE ID_usr=?'
        self.PhotoChange='UPDATE User_data SET Avatar = ? Where ID_usr = ?'
        self.onforegin='PRAGMA foreign_keys = ON'

    def init__(self):
        self.get_dop='''SELECT User_info.Birhtday,User_info.City_birthday,User_info.City_live 
        FROM User_data,User_info
        WHERE User_data.ID_usr=?;'''
        self.dopINS="INSERT INTO User_info (ID_usr) VALUES (?)"
        self.setings_name="UPDATE User_data SET Name = ? Where ID_usr = ?"
        self.setings_surname="UPDATE User_data SET Surname = ? Where ID_usr = ?"
        self.setings_password="UPDATE User_data SET Password = ? Where ID_usr = ?"
        #-------------------------------------------------------------------------------
        self.setings_brth="UPDATE User_info SET Birhtday = ? Where ID_usr = ?"
        self.setings_city_l="UPDATE User_info SET City_live = ? Where ID_usr = ?"
        self.setings_city_b="UPDATE User_info SET City_birthday = ? Where ID_usr = ?"
        self.setings_email="UPDATE User_info SET Email = ? Where ID_usr = ?"
        self.setings_number="UPDATE User_info SET Nomber = ? Where ID_usr = ?"
        
    def get_dop_info(self,id):
        self.cursor.execute(self.get_dop,(id,))
        records=self.cursor.fetchall()
        return records[0]
        
    def create_table(self):
        try:
            self.cursor.execute(self.Table_user)
            self.connect.commit()
            print("Table User_data write")
        except:
            print("Table User_data was created")
        try:
            self.cursor.execute(self.Table_user_info)
            self.connect.commit()
            print("Table User_user_info write")
        except:
            print("Table User_user_info was created")
        try:
            self.cursor.execute(self.onforegin)
            self.connect.commit()
        except:
            pass

    def get_ava(self,login):
        self.cursor.execute(self.Select_ava,(login,))
        records=self.cursor.fetchall()
        if records!=[]:
            return records[0][0]
        else:
            return None
            
    def reg_user(self,login,name,surname,password):
        self.cursor.execute(self.Select_login,(login,))
        records=self.cursor.fetchall()
        if records!=[]:
            return False
        else:
            id=os.urandom(random.randint(5,20)).hex()
            self.cursor.execute(self.INSERT,(id,login,name,surname,password,ava))
            self.connect.commit()
            self.cursor.execute(self.dopINS,(id,))
            self.connect.commit()
            return True
    
    def vhod_user(self,login,password):
        self.cursor.execute(self.Select,(login,password))
        records=self.cursor.fetchall()
        if records==[]:
            return False
        else:
            return True
    
    def get_id_user(self,login):
        self.cursor.execute(self.Select_id,(login,))
        records=self.cursor.fetchall()
        if records==[]:
            return None
        else:
            return records[0][0]
    
    def get_info(self,id):
        self.cursor.execute(self.Select_all,(id,))
        records=self.cursor.fetchall()
        if records!=[]:
            return records[0]
        else:
            return None
    
    def list_users(self):
        self.cursor.execute(self.Select_all2)
        records=self.cursor.fetchall()
        data=[len(records)]
        data.append([random.choice(records) for i in range(15)])
        return data
    
    def change_ava(self,file,id):
        self.cursor.execute(self.PhotoChange,(file,id))
        self.connect.commit()
    
    def get_name(self,id):
        self.cursor.execute(self.Select_name,(id,))
        records=self.cursor.fetchall()
        return records[0][0]
        
    def settings_ch(self,data,id):
        if "name" in data:
            self.cursor.execute(self.setings_name,(data["name"],id))
            self.connect.commit()
        elif "surname" in data:
            self.cursor.execute(self.setings_surname,(data["surname"],id))
            self.connect.commit()
        elif "password" in data:
            self.cursor.execute(self.setings_password,(data["password"],id))
            self.connect.commit()
        elif "city_b" in data:
            self.cursor.execute(self.setings_city_b,(data["city_b"],id))
            self.connect.commit()
        elif "city_l" in data:
            self.cursor.execute(self.setings_city_l,(data["city_l"],id))
            self.connect.commit()
        elif "pochta" in data:
            self.cursor.execute(self.setings_email,(data["pochta"],id))
            self.connect.commit()
        elif "number" in data:
            self.cursor.execute(self.setings_number,(data["number"],id))
            self.connect.commit()
    
    def such(self,name):
        self.cursor.execute(self.Select_such,(name,))
        return self.cursor.fetchall()
    
    def __del__(self):
        self.connect.close()