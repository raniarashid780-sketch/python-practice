"""
14_shutil_practice.py

Practice script combining pathlib's collision-resolution logic with
shutil.move() to actually move files. Reuses the collision-safe
naming loop from 13_pathlib_practice.py, then moves each file into
test_output instead of only detecting/printing.

Groundwork for the overwrite-prevention fix in file-organizer-automation
(Bug 1: silent overwrite on filename collision).
"""
import pathlib
import shutil

path = pathlib.Path.home() / "Downloads" / "test_folder"
output_folder = path / "test_output"
path.mkdir(parents=True, exist_ok=True)
output_folder.mkdir(parents=True, exist_ok=True)

for file in path.glob("*"):
    if file.is_file():
        safe_destination = output_folder / file.name
        counter = 1
        while safe_destination.exists():
            safe_destination = output_folder / f"{file.stem} ({counter}){file.suffix}"
            counter += 1

        print(f"Moving {file.name} -> {safe_destination}")
        shutil.move(file, safe_destination)