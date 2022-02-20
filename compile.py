from os import system


files =  [
    "src\\About.py",
    "src\\Begin.py",
    "src\\Board.py",
    "src\\Check.py",
    "src\\Direction.py",
    "src\\EndProg.py",
    "src\\EvalCoord.py",
    "src\\EvalWeights.py",
    "src\\GameBoard.py",
    "src\\IA.py",
    "src\\Info.py",
    "src\\main.py",
    "src\\Node.py",
    "src\\Start.py",
    "src\\Turn.py",
    "src\\Win.py",
]

files_list = ""
for file in files:
    files_list += " " + file

system("pip install pyinstaller")
system("pyinstaller" + files_list + " --name pbrain-gomoku-ai.exe --onefile")
system('copy .\\dist\\pbrain-gomoku-ai.exe .')