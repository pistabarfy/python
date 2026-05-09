from pathlib import Path
p = Path('./notes.txt')
info = p.stat()
 
info.st_size   # File size in bytes
info.st_mtime  # Last modified time (as a Unix timestamp number)
info.st_ctime  # Created time (on Windows) or metadata change time (on Linux)
info.st_mode   # File permissions (as a number — more on this in chmod section)
