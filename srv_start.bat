@echo off
Title Server running
start /B python main.py
start /B src\db\smsbecuper.py
:start "" python cmd.py
:start "" ngrok.exe http 5000
:or start /B
:/MIN to no window