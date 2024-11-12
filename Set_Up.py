import subprocess
import sys

# List of required packages
required_packages = [
    "PyQt5",
    "pyqtdarktheme",
    "numpy",
    "requests"
]

# Function to install packages
def install_packages():
    for package in required_packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"'{package}' installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error occurred while installing '{package}'.")

if __name__ == "__main__":
    install_packages()
