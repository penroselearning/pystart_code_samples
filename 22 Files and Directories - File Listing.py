import os
basedir = os.path.abspath(os.path.dirname(__file__))
files = []
for r, d, f in os.walk(basedir):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    print(f)