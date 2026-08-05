"""
13_pathlib_practice.py

Practice script for the pathlib library. Scans a folder and, for each
file, prints its name, extension, stem, size in KB, and whether a file
with the same name already exists in a separate output folder.

No files are moved or modified — detection only. This is a warm-up
for the overwrite-prevention logic needed in file-organizer-automation
(Bug 1: silent overwrite on filename collision).
"""
import pathlib
path = pathlib.Path.home() / "Downloads" / "test_folder"

output_folder = path / "test_output"
path.mkdir(parents=True, exist_ok=True)
output_folder.mkdir(parents=True, exist_ok=True)


for file in path.glob("*"):
    if file.is_file():
        test_path = output_folder / file.name
        counter = 1
        while test_path.exists():

            test_path = output_folder / f"{file.stem} ({counter}){file.suffix}"
            counter += 1
        print(f"Final resolved path: {test_path}")
        test_path = output_folder / file.name
        print(f"Name of the file is : {file.name}")
        print(f"File extension is : {file.suffix}")
        print(f"File stem is : {file.stem}")
        print(f"File size is : {file.stat().st_size/1024:.2f} KB")
        print(f"Already in output folder? : {test_path.exists()}")
