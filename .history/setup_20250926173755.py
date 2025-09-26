import sys
import subprocess
import os
from setuptools import setup, find_packages

# The following code was generated with assistance from Anthropic's Claude 3.7 (2025) AI language model
# and Google's Gemini 2.5 Pro (2025) AI language model.
# Define the path to your main script
script_path = 'classPrototype2.py'

# 
# Function to run PyInstaller
def build():
    # Get the absolute path to the current directory
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Use os.pathsep to get the correct separator (';' on Windows, ':' on macOS/Linux)
    separator = os.pathsep
    
    # Command to run PyInstaller
    command = [
        'pyinstaller',
        '--onefile',              # Package into a single executable
        '--windowed',             # No console window
        '--name=NoteTranspositionProgram',  # Name of the executable
        
        # Add Python module dependencies
        f'--add-data={os.path.join(current_dir, "ImageHoverWidget2.py")}{separator}.',
        f'--add-data={os.path.join(current_dir, "resource_utils.py")}{separator}.',
        
        # Add all image files with the correct path separator
        f'--add-data={os.path.join(current_dir, "altoclef.png")}{separator}.',
        f'--add-data={os.path.join(current_dir, "arrow.png")}{separator}.',
        f'--add-data={os.path.join(current_dir, "bassclef3.png")}{separator}.',
        f'--add-data={os.path.join(current_dir, "flat.png")}{separator}.',
        f'--add-data={os.path.join(current_dir, "natural.png")}{separator}.',
        f'--add-data={os.path.join(current_dir, "sharp.png")}{separator}.',
        f'--add-data={os.path.join(current_dir, "trebelclef.png")}{separator}.',
        f'--add-data={os.path.join(current_dir, "wholenote.png")}{separator}.',
        
        # Add a hook to handle resource paths
        '--additional-hooks-dir=.',
        
        script_path
    ]
    
    # Run the command
    try:
        print("Starting build process...")
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Build completed successfully!")
        else:
            print("Build failed with error:")
            print(result.stderr)
            
    except Exception as e:
        print(f"An error occurred during build: {str(e)}")

# Only run the build function if this script is executed directly
if __name__ == '__main__':
    if sys.platform == 'win32':
        print("Building executable for Windows...")
        build()
    elif sys.platform == 'darwin':
        print("Building executable for macOS...")
        build()
    else:
        print("This script is intended to build executables on Windows or macOS only.")
        print(f"Current platform: {sys.platform}")
    # Exit after building to prevent setup() from running
    sys.exit(0)
