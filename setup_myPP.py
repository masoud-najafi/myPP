import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["wx", "myPP"],
    "excludes": ["tkinter"],
    "include_files": [],
    "path": sys.path + ["src"]
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="myPP",
    version="0.1.0",
    description="MyPP Application",
    options={"build_exe": build_exe_options},
    executables=[Executable(
        "src/myPP/A/main.py",
        base=base,
        target_name="myPP.exe",
        icon=None  # You can add an icon path here if desired
    )],
    package_dir={"": "src"},
    packages=["myPP", "myPP.A", "myPP.B"]
)