import os
#   Переменные
DEBUG=True
HOSTS="0.0.0.0"
PORT=1478
SECRET_KEY=os.urandom(40).hex()
DATEBASE="test"

# Адреса
MAIN_ADRES="/Python_Social_WEB"
USER=f"{MAIN_ADRES}/users" #id
UPLOAD_FILE=f"{MAIN_ADRES}/anothermoves/uploadfile"
AVA=f"{MAIN_ADRES}/anothermoves/getava"
MESSAGES=f"{MAIN_ADRES}/sms"#+user
SETTINGS=f"{MAIN_ADRES}/settings"#+id