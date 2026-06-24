"""
File Organizer Automation

This program organizes files from a source folder into different
categories based on their file extensions.

Author: Your Name
"""

from pathlib import Path
from dataclasses import dataclass
from datetime import datetime
import shutil

# ==========================
# Configuration
# ==========================

@dataclass(frozen=True)
class Config:
    source_folder: Path
    destination_folder: Path
    dry_run: bool = True


# ==========================
# File Categories
# ==========================

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".ps1"],
    "Code": [".java", ".c", ".cpp", ".cs", ".html", ".css", ".php", ".rb"],
}


# ==========================
# Helper Functions
# ==========================

def get_category(extension):
    """Return the category name based on the file extension."""
    extension = extension.lower()

    for category, extensions in EXTENSION_MAP.items():
        if extension in extensions:
            return category

    return "Others"


def unique_destination(destination: Path):
    """
    Prevent overwriting files.

    Example:
    report.pdf
    report(1).pdf
    report(2).pdf
    """

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = f"{destination.stem}({counter}){destination.suffix}"
        new_destination = destination.with_name(new_name)

        if not new_destination.exists():
            return new_destination

        counter += 1


def write_log(message, log_file):
    """Append messages to a log file."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


# ==========================
# Main Function
# ==========================

def organize_files(config: Config):

    if not config.source_folder.exists():
        print("Source folder does not exist.")
        return

    config.destination_folder.mkdir(parents=True, exist_ok=True)

    log_file = config.destination_folder / "organizer.log"

    total_files = 0
    moved_files = 0

    print("=" * 60)
    print("FILE ORGANIZER")
    print("=" * 60)

    for item in config.source_folder.iterdir():

        if not item.is_file():
            continue

        total_files += 1

        category = get_category(item.suffix)

        destination_folder = config.destination_folder / category

        destination_folder.mkdir(parents=True, exist_ok=True)

        destination_file = destination_folder / item.name

        destination_file = unique_destination(destination_file)

        if config.dry_run:
            print(f"[DRY RUN]")
            print(f"{item}")
            print(f"   → {destination_file}\n")

        else:
            shutil.move(str(item), str(destination_file))

            moved_files += 1

            log_message = f"Moved: {item.name} -> {destination_file}"

            print(log_message)

            write_log(log_message, log_file)

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print(f"Total files found : {total_files}")

    if config.dry_run:
        print("Mode              : DRY RUN")
        print("Files moved       : 0")
    else:
        print(f"Files moved       : {moved_files}")

    print("=" * 60)


# ==========================
# Program Entry Point
# ==========================

if __name__ == "__main__":

    config = Config(
        source_folder=Path("/run/media/awongo-fahadi-rashid/AFRAH/Downloads"),
        destination_folder=Path("/run/media/awongo-fahadi-rashid/AFRAH/Desktop/OrganizedFiles"),
        dry_run=False      # Change to False to actually move files
    )

    organize_files(config)