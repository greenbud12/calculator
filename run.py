#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: run.py
Description: Installs requirments and runs calculator.py.
Author: Bailey Bakerson
Date: 2023-02-24
"""

import os
import subprocess


if __name__ == "__main__":
    # Check if setup flag file exists
    if os.path.exists('setup_complete.txt'):
        print('Setup already completed')
    else:
        # Install requirements
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

        # Create setup flag file
        open('setup_complete.txt', 'a').close()
        print('Setup complete')

    # Run a Python file
    subprocess.check_call(['python', 'src\calculator.py'])