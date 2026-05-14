from pathlib import Path
p = Path('./io/file.txt')
try: 
    with open(p,"a") as f:
     print(f.write("Parvardigaaar!!!"))
except FileNotFoundError:
   print("Plz add a file dawg")
except PermissionError:
   print("Plz Modify the permission dawg")