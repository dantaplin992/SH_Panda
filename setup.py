from setuptools import setup
import platform

sys = platform.system()
if sys == "Windows":
    plat = ["win_amd64"]
else:
    plat = ["win_amd64", "macosx_10_9_x86_64"]

setup(
    name='p3dtest',
    options={
        'build_apps': {
            # Build asteroids.exe as a GUI application
            'gui_apps': {
                'p3dtest': 'main.py',
            },

            # Set up output logging, important for GUI apps!
            'log_filename': '$USER_APPDATA/p3dtest/output.log',
            'log_append': False,

            # Specify which files are included with the distribution
            'include_patterns': [
                '**/*.png',
                '**/*.jpg',
                '**/*.egg',
                '**/*.bam',
                '**/*.ttf',
            ],

            # Include the OpenGL renderer and OpenAL audio plug-in
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],

            'platforms': plat,
        }
    }
)