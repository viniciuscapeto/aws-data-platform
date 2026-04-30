@echo off
cd /d C:\Users\cso6493\Documents\aws_data_platform
call venv\Scripts\activate
set PYTHONPATH=.
python pipeline\collector.py