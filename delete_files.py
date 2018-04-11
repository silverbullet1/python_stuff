# Delete a set of specific files in a folder recursively
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-p', '--path', required = True, help = 'Path to the folder')
ap.add_argument('-f', '--files', nargs = '*', required = True, help = 'File names')
args = vars(ap.parse_args())

# traverse root directory, and list directories as dirs and files as files
for root, directories, filenames in os.walk(args["path"]):
	for filename in filenames:
		for current_file in args["files"]:
			if filename == current_file:
				os.remove(os.path.join(root,filename))
				print("Removed file : {}".format(os.path.join(root,filename)))
