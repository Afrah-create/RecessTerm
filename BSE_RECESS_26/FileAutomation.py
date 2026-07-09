# Automation and Webscrapping

# What is Automation in Python?

'''
The Automation Pipeline:

Input -> , Transform -> , Output -> , Reliability -> Run


# Key Libraries for Auomation
Library 
pathlib - file path
shutil - copy , move, archive
Schedule - task Schduling
Watchdog  - File System events monitoring
openpyxl - Excel file read / write


'''

# Example 4 / File Automation
# File Automation # Organising files on our computer

# Get the file Path Downloads
# File path 
# Approach : pathlib

# from pathlib import Path

# # Old ways using the (os.path)
# import os
# file_path = os.path.join(os.path.expanduser("~"), "Downloads", "report.pdf")


# # New Way of (pathlib)
# file_path = Path.home() / "Downloads" / "report.pdf"


# File Organisation Script
# Real we can automatically organiseed a Download folder by file type

# !/usr/bin

# Import libraries
from pathlib import Path
import shutil
from datetime import datetime
from dataclasses import dataclass

# --Configuration
@dataclass(frozen=True)
class Config:
    source_dir: Path
    destination_dir: Path
    dry_run: bool = True

EXTENSION_MAP = {
    'Images': [".jpg", ".jpeg" , ".png", ".svg"],
    'Documents': [".pdf", ".docx", ".txt"],
    'Videos': [".mp4", ".mkv", "mov"],
    'Code': [".py", ".js", ".html"],
    'Archives': [".zip", ".tar.gz"],


}
# Assignment 2: Write a python script that perfoms file ogranisation of your download folder
# Code Logic for File Automation
def get_target_category(filepath: Path) -> str:
    pass