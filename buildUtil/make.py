import os
import platform

sys = platform.system()
if sys == "Windows":
    os.system("ppython setup.py build_apps")
else:
    os.system("python3 setup.py build_apps")
