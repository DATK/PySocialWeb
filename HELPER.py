from src.SQL import SQL
from src.config import *
import random
import os

sql=SQL(DATEBASE)

def add_user(n,prnt=True):
    for i in range(n):
        name=f"BOT{i}"
        surname=f"BOT{i}"
        login=f"Bot_Login{random.randint(100,50000)}"
        password=os.urandom(9)
        if sql.reg_user(login,name,surname,password):
            if prnt:
                print(f"{login} created")
            
            
       
       
add_user(1000000,False)            
input()