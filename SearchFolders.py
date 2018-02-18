import os

import sys


def scan_and_remove(path, mode):
	counter = 0
	for root, directories, filenames in os.walk(path):
		for directory in directories:
			if mode == 'scan':
				# print(os.path.join(root, directory))
				if os.listdir(os.path.join(root, directory)) == []:
					counter += 1
			if mode == "remove":
				if os.listdir(os.path.join(root, directory)) == []:
					os.rmdir(os.path.join(root, directory))
					counter += 1
	return counter


def main(argv):
	path = input("Please sepcify path to scan for empty directories: ")
	yes_for_all = False
	found = 0
	while scan_and_remove(path, "scan"):
		found = scan_and_remove(path, "scan")
		print(str(found) + " empty directories have been found.")
		if not yes_for_all:
			answer = input("Do you want to remove them? (Y/N/YFA (yes for all)?")
			if answer == "YFA" or answer == "yfa":
				yes_for_all = True
		if answer == "Y" or answer == "y" or yes_for_all:
			num = scan_and_remove(path, "remove")
			if num > 0:
				print(str(num) + " empty directories have successfully been removed!")
		else:
			print("No directories were deleted.")
			break
	if found == 0:
		print("No empty directories to remove.")
	print("My work here is done. Good Bye!")
if __name__ == "__main__":
	main(sys.argv)
