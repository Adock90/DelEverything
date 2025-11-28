@echo off


:parse

:endparse

echo [DelEverything.bat] Starting main.py and Python.exe

cd src

python.exe ./main.py "%~1"

cd ..

echo [DelEverything.bat] Bye

timeout 1 > NUL

@echo on