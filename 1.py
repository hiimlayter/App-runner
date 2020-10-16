import sys
import os
x = os.path.abspath(sys.argv[0]).split("\\")[-1]
command = 'cmd /c "python app-runner.py "'
x = x.replace(".py","")
command = command+x
os.system(command)
