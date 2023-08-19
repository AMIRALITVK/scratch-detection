from cx_Freeze import setup, Executable

setup(
    name="Scratch-Detector",
    version="1.0",
    description="Scratch detector application",
    executables=[Executable("opencv.py")]
)
