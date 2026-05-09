from pathlib import Path


p = Path("Hanafi 1 Is'af al Murideen.pdf")
print(p)

# to check what exists: 

print(p.exists())
# to check whether the file exists.

print(p.is_dir())
# to check whether the pointed path is a directory

print(p.is_file())
# to check whether the pointed path is a file

print(p.is_symlink())
# to check the pointed file is a shortcut (system link)

print(p.is_mount())
# to check the path leads to a mount point (as of a usb)

print(p.is_socket())
# to check whether the path leads to a socket file (networking)

print(p.is_fifo())
# to check whether the path leads to a process pipeline (First in first out)

info = p.stat()
print(info)