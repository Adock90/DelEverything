@echo off

echo [DelEverything.bat] Starting main.py and Python.exe

cd src

python.exe ./main.py

cd ..

echo [DelEverything.bat] Bye

timeout 1 > NUL

cls