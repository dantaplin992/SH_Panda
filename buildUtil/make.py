import os
import platform

sys = platform.system()
if sys == "Windows":
    os.system("ppython setup.py build_apps")
else:
    os.system("python setup.py build_apps")
