# Panda3D App

An attempt at re-making the same game for the 1000th time, but using
Panda3D and Python this time instead of Typescript, BabylonJS and 
Electron


## Requirements

This project requires an installation of Panda3D, with the versions
of python and pip that come bundled with it


## Compiling

To compile and package the project, run the following command:

```ppython setup.py build_apps```

The project is set up to only package for Windows, but others can be
added to the 'platforms' array in `setup.py`
