@echo off
set /p filepath="enter filepath: "
gpg --verify %filepath
