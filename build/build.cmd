@echo off
cd /d %~dp0
del robot.exe > nul
echo Building.
pyinstaller --upx-dir upx\Windows\ -F robot.py -i logo.ico
move dist\*.exe dist\..
choice /t 1 /d y /n > nul
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q __pycache__
del /f /s /q *.spec
echo Zipping.
upx\Windows\upx.exe --ultra-brute robot.exe
echo Finished.
pause