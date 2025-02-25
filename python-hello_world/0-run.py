#!/usr/bin/python3
import os
import sys

# Ensure PYFILE environment variable is set
pyfile = os.getenv('PYFILE')
if not pyfile:
    print("Error: PYFILE environment variable is not set.")
    sys.exit(1)

# Execute the Python file
os.system(f'python {pyfile}')