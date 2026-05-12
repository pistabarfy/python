from pathlib import Path
while True:

    print("Welcome to File Organiser")
    path = input("Enter the proper path : ")
    filepath = Path(path)
    if filepath.exists == False:
        print("Enter Proper Path")

    file_mapping = {
    ".py":"code",
    ".js":"code",
    ".html":"code",
    ".c":"code",
    ".jpg":"images",
    ".jpeg":"images",
    ".png":"images",
    ".webp":"images",
    ".mp4":"videos",
    ".mp3":"audios",
    ".wav":"audios",
    ".mkv":"videos",
    ".mov":"videos",
    ".pdf":"readables",
    ".docx":"readables",
    ".deb":"installables",
    ".sh":"installables",
    "AppImage":"installable",
    ".zip":"archives",
    ".tar":"archives",
    ".rar":"archives",
    "":"unknown"
    }
    
    for files in filepath.iterdir():
        file_name = files.stem
        extension = files.suffix
        print(f"{files.name} and the {extension}")
        destination = file_mapping.get(extension, "unknown")
        target = Path('/home/sahil/Downloads/') / destination
        target.mkdir(exist_ok=True)
        files.rename(target / files.name)
            

    


    

