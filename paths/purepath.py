from pathlib import PurePath
"""PurePath object manipulates the path of the fucking filesystems, files and folders only as strings. Path does the same, but it also manipulates actually filesystems, files, folders, renames, reads, writes and checks.
"""


p = PurePath("/home/sahil/Desktop/maliki fiqh/Hanafi 1 Is'af al Murideen.pdf")

print(p.drive)
#returns a void coz drive is dark af

print(p.root)

#returns a slash coz in unix based systems teh the root is '/'
print(p.anchor)

print(p.stem)
#return the final part of the / it could be a folder or a file

print(p.parent)
# returns the parents of the final folder or file

print(p.parents[1])
#returns the parents of the folder/file and its parent folder [..] and so on

print(p.name)
#returns the file name without any extension name


print(p.parts)
#returns the entire string of path as a array (Each folder, and file)

print(p.suffix)
#returns teh extension or filetype

print(p.suffixes)
#returns the file types adn extension of many files as a damn array



# methods of pure path

print(p.is_absolute())

# checks whether the filepath starts from teh route or not

print(p.is_relative_to("/"))

#checks whether the fiel is in a fileepath or not

