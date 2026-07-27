import math
import re
from datetime import datetime
from pathlib import Path


def sort_file(directory_path):
    dir_path = Path(directory_path)
    
    if not dir_path.is_dir():
        print(f"Error: {directory_path} is not a valid directory.")
        return

    files = [f for f in dir_path.iterdir() if f.is_file()]
    print("Files found:", [f.name for f in files])
    
    for full_file_path in files:
        if full_file_path.exists():
            timestamp = full_file_path.stat().st_mtime
            file_date = datetime.fromtimestamp(timestamp)
            
            # Get Month name and Day number
            month_name = file_date.strftime("%B") 
            day_num = file_date.day               
            
            # Calculate week number
            week_num = math.ceil(day_num / 7)      
            week_folder_name = f"Week_{week_num}"  
            
            target_folder = dir_path / month_name / week_folder_name
            
            target_folder.mkdir(parents=True, exist_ok=True)
            
            # Move the file into its new folder
            new_file_location = target_folder / full_file_path.name
            full_file_path.rename(new_file_location)
            
            print(f"Moved {full_file_path.name} to {month_name}/{week_folder_name} (Day: {day_num})")
            
        else:
            print(f"File not found: {full_file_path.name}")
            
months_pattern = re.compile(
    r'^(January|February|March|April|May|June|July|August|September|October|November|December|'
    r'jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)$', 
    re.IGNORECASE
)

def sort_folder(directory_path):
    dir_path = Path(directory_path)
    
    if not dir_path.is_dir():
        print(f"Error: {directory_path} is not a valid directory.")
        return
    
    folders = [f for f in dir_path.iterdir() if f.is_dir()]
    print("Folders found:", [f.name for f in folders])
    
    for full_folder_path in folders:
        if full_folder_path.exists():
            
            # apply the regex check if match the name then skip it
            if months_pattern.match(full_folder_path.name):
                print(f"Skipping script-made month folder: {full_folder_path.name}")
                continue  
                
            timestamp = full_folder_path.stat().st_mtime
            file_date = datetime.fromtimestamp(timestamp)
            
            # Get Month name and Day number
            month_name = file_date.strftime("%B") 
            day_num = file_date.day               
            
            # Calculate week number
            week_num = math.ceil(day_num / 7)      
            week_folder_name = f"Week_{week_num}"  
            
            target_folder = dir_path / month_name / week_folder_name
            target_folder.mkdir(parents=True, exist_ok=True)
            
            new_folder_location = target_folder / full_folder_path.name
            full_folder_path.rename(new_folder_location)
            
            print(f"Moved folder '{full_folder_path.name}' to {month_name}/{week_folder_name} (Day: {day_num})")
            
        else:
            print(f"Folder not found: {full_folder_path.name}")

     

