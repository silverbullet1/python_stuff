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
completed = False


def move_file(filename, foldername):
	success = False
	if not os.path.exists(foldername):
		try:
			os.mkdir(foldername)
		except:
			print("\nCould not create folder. Check for permissions or disk space.")

	try:
		shutil.move(filename, foldername)
		success = True
	except shutil.Error:
		print("File {} already exists. Press 1 to skip or 2 to rename it".format(filename))
		choice = int(raw_input())

		if choice == 1:
			return
		else:
			print("\nEnter new name for file with extension : ")
			while success is False:
				new_name = raw_input()
				path, last_name = os.path.split(filename)
				newpath = os.path.join(path, new_name)
				if not os.path.exists(newpath):
					os.rename(filename, newpath)
					filename = newpath
					print("\nFile rename successful to {}.".format(filename))
					success = True
				else:
					print("\nPlease try another filename.")
	print("\n{} was moved to {}".format(os.path.split(filename)[-1],os.path.split(foldername)[-1]))


def cleanup():
	print("\nPress 1 to delete empty folders left behind (if any)? and 0 to exit")
	choice = int(raw_input())
	if choice == 1:
		for root, directories, filenames in os.walk(args["path"]):
			for directory in directories:
				if directory not in folders:
					print("\nRemoving folder {}".format(directory))
					os.rmdir(os.path.join(args["path"],directory))
		print("\nCompleted!!")


def main():
	completed = False
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
				completed = True
	return completed


completed = main()
if completed is True:
	print("\nFile organization successful!!\n")
	cleanup()
else:
	print("\nFiles are already organized!!")