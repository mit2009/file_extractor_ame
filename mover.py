import pickle
import os
from subprocess import call

# build structure

def expandFolder(folder):
	files = []
	for element in os.listdir(folder):
		if os.path.isdir(folder + "/" + element):
			files.extend(expandFolder(folder + "/" + element))
		else:
			if element[-3:].lower() in ["mov", "mts", "m4v", "mp4"]:
				files.append(folder + "/" + element)
	return files

baseFolder = 'BuildChallenge'

files = expandFolder(baseFolder)

print(len(files))

print(files)

print(len(files))

# folder.replace("/", "__") + "__" + element)

# pickle structure

pickle.dump(files, open("initial_structure.pkl", "wb"))

# move files

for f in files:
	call(["mv", f, "to_encode/" + f.replace("/", "__")])

# move files back