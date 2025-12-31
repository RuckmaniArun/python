import os
from pathlib import Path
import shutil

print("List directory files")
print(os.listdir())

source_dir=Path("C:/Users/arun/Downloads")
print(source_dir)

p=Path("chances.csv")
print(p.resolve())

File_Categories={

    "PY_Image": [".png",".jpeg",".jpg"],
    "PY_PDF": [".pdf"],
    "PY_MS Documents": [".docx"],
    "PY_Other Files": [".txt"]
}

def create_folder():
    for category in File_Categories:
        folder=source_dir / category
        folder.mkdir(exist_ok=True)
        print("Folder Created", folder)
    
    #Handling other files
    Other_folder=source_dir / "PY_Others"
    Other_folder.mkdir(exist_ok=True)
    
        
def verify_SourcePath_exists():
    if not source_dir.exists():
        return False
    return True
    
def get_Extension(extension):
    for category, file_extensions in File_Categories.items():
        if extension.lower() in file_extensions:
            return category
    return "PY_Others"
    
def organize_files():
    for items in source_dir.iterdir():
        
        #Skipping folders
        if items.is_dir():
            Print("Folders are skipped for migration")
            continue
            
        extension=items.suffix
        print(f"Items {items} extension is {extension}")
        category_extension=get_Extension(extension)
        
        target_folder=source_dir / category_extension
        target_path=target_folder / items.name
        
        try:
            print(f"Moving the file {items.name} to category")
            shutil.move(str(items), str(target_path))
        except Exception as ex:
            print(f"Error moving {items.name}")
        
    
def migrate():
    if verify_SourcePath_exists():
        print("*******Proceed for folder creation********")
        create_folder()
        organize_files()
    else:
        print("Source path does not exists")
        
migrate()
