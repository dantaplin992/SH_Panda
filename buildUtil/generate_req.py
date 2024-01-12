import os
import platform

sys = platform.system()
if sys == "Windows":
    os.system("ppython -m pip freeze > requirements.txt")
else:
    os.system("python -m pip freeze > requirements.txt")