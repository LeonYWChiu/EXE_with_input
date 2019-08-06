import sys


if __name__ == '__main__':
	
	file_name =sys.argv[1]
	file = open(file_name, 'r')
	print(file.read())
	input()