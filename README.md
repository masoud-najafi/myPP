# myPP
a package to show the way PyPI and Windows executable is generated.
The package is a sample Python package that demonstrates a wxPython message box with a modular structure.

## the myPP project structure 
Here's how to build a simple Python project using the src/ layout, and use setuptools with a setup.py file to create a command-line executable.
```
myPP_project/
├── src/
│   └── myPP/
│       ├── A/
│       │   ├── __init__.py
│       │   └── main.py
│       ├── B/
│       │   ├── __init__.py
│       │   └── helper.py
│       └── __init__.py
├── pyproject.toml
├── setup_myPP.py
├── README.md
└── LICENSE
└── requirements.txt
```
## Before installing
Before installing the myPP project you may run this to install the required packages.
Usually pip install the required packages mentionned in the pyproject.toml
```bash
pip install -r requirements.txt
```

## testing the code without installing

you need to give the path of the uninstalled package to be used by Python

```bash
#method 1) without changing PYTHONPATH
cd D:\ttx\myPP\src
python -m  myPP.A.main  arg1 arg2 # not good: because main.py is expected to be imported not executed 
python -m  myPP         arg1 arg2 # good:     __main__.py is called and executed

```

```bash
#method 2) with  changing PYTHONPATH
set PYTHONPATH=%PYTHONPATH%;D:\ttx\myPP\src
python D:\ttx\myPP\src\myPP\A\main.py    arg1 arg2 #main.py has been called
python D:\ttx\myPP\src\myPP\__main__.py  arg1 arg2 # __main__.py has been called.
```


## Installation

1. Install the package:
   ```bash
   pip install .
   pip show myPP
   ```
## test the installtion 

   ```bash
   pip show myPP
   python -c "import myPP;myPP.show_message_box()"


   ```
## uninstalling the project on the machine 

   ```bash
   pip show myPP
   pip uninstall myPP
   ```
 
2. Run the application:
   ```bash
   myPP
   ```

## Building Executable

To create a Windows executable using CX_Freeze:

```bash
python setup_myPP.py build   
python setup_myPP.py bdist_msi
```

The executable will be created in the `build` directory.