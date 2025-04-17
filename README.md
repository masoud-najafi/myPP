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


## Installation

1. Install the package:
   ```bash
   pip install .
   pip show myPP
   python -c "import myPP;myPP.show_message_box()"
   ```
## test the installtion 

   ```bash
   pip show myPP
   python -c "import myPP;myPP.show_message_box()"
   ```
## uninstalling the project on the machine 

   ```bash
   pip show myPP
   pip uininstall myPP
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
