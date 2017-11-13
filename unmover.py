import os
import pickle
from subprocess import call

files = pickle.load(open("initial_structure.pkl", "rb"))

for f in files:
	call(["mv", f.replace("/", "__"), f])