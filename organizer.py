# Organize clustered data in a directory
import os
import argparse
import shutil

ap = argparse.ArgumentParser()
ap.add_argument('-p', '--path', required=True, help='Path to the folder')

# Popular file formats list
executables = ['exe', 'msi']
compressed = ['zip', 'rar']
documents = ['txt', 'rtf', 'doc', 'docx', 'html', 'css', 'xml', 'odt', 'pdf']
photos = ['jpeg', 'jpg', 'bmp', 'png', 'gif', 'tiff', 'gif', 'bmp', 'svg']
videos = ['avi', 'mov', 'mp4', 'wmv', 'webm', 'mpg', 'flv', 'vob', 'mkv', 'm4v']
music = ['mp3', 'aac', 'wav']
folders = ['Programs', 'Music', 'Videos', 'Photos', 'Documents', 'Compressed', 'Others']
args = vars(ap.parse_args())


def move_file(filename, foldername):
	success = False

	if not os.path.exists(foldername):
		try:
			os.mkdir(foldername)
		except:
			print("Could not create folder. Check for permissions or disk space.")

	while (success != True):

		try:
			shutil.move(filename, foldername)
			success = True

		except shutil.Error:
			print("File {} already exists. Press 1 to skip or 2 to rename it".format(filename))
			choice = int(raw_input())

			if choice == 1:
				return

			else:
				print("Enter new name for file with extension : ")
				new_name = raw_input()
				path, last_name = os.path.split(filename)
				newpath = os.path.join(path, new_name)
				os.rename(filename, newpath)
				filename = newpath
				print("File rename successful to {}!".format(filename))


for root, directories, filenames in os.walk(args["path"]):
	path, folder_name = os.path.split(root)
	if folder_name not in folders:  # To avoid creation of infinite subfolders, do not explore these folders
		for filename in filenames:
			extension = os.path.splitext(filename)[1]
			extension = extension[1:].lower()  # remove the dot

			if extension in executables:
				move_file(os.path.join(root, filename), os.path.join(args["path"], "Programs"))
			elif extension in compressed:
				move_file(os.path.join(root, filename), os.path.join(args["path"], "Compressed"))
			elif extension in documents:
				move_file(os.path.join(root, filename), os.path.join(args["path"], "Documents"))
			elif extension in photos:
				move_file(os.path.join(root, filename), os.path.join(args["path"], "Photos"))
			elif extension in music:
				move_file(os.path.join(root, filename), os.path.join(args["path"], "Music"))
			elif extension in videos:
				move_file(os.path.join(root, filename), os.path.join(args["path"], "Videos"))
			else:
				move_file(os.path.join(root, filename), os.path.join(args["path"], "Others"))

print("Press 1 to delete empty folders left behind (if any)? and 0 to exit")
choice = int(raw_input())
if choice == 1:
	for root, directories, filenames in os.walk(args["path"]):
		for directory in directories:
			if directory not in folders:
				print "Removing ", directory
				os.rmdir(os.path.join(args["path"],directory))