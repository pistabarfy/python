from pathlib import Path

p = Path('python/paths/text.txt')
print(p)
# pointing towards a file

print(Path().home())
#initialises at the home directory
print(Path().cwd().absolute())
# initialises at the currrent directory (from the root)
print(Path('Documents/'))
#initialises from the documents folder



