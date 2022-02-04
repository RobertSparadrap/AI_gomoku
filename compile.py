import os

os.system("pip install pyinstaller")
os.system("pyinstaller pbrain_gomoku_main.py --name pbrain-gomoku.exe --onefile")
os.system('copy .\\dist\\pbrain-gomoku.exe .')