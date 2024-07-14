import json
import time

file="./src/db/Messanges.json"
def backuper(file):
    while True:
        try:
            with open(file,"r",encoding="UTF-8") as f:
                data=json.load(f)
            print("data succses writed")
        except:
            with open(file,"w",encoding="UTF-8") as f:
                json.dump(data,f)
            print("data rewrite, error")
        time.sleep(2)

backuper(file)