from pathlib import Path

p = Path("sahil/")

q = p/Path("Desktop/")/Path("maliki fiqh/")

#we uses slashes to join paths literally

r = p/"Desktop"/Path("maliki fiqh/")/"Hanafi 1 Is'af al Murideen.pdf"

#we can even add "string" of file names or folders together with these slashes

print(f"{p} \n {q} \n {r}")