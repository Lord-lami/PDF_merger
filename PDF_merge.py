import PyPDF2
import sys

file_seq = sys.argv[1:]
unifier = PyPDF2.PdfMerger()
if __name__ == '__main__':
	for file in file_seq:
		unifier.append(file)
	name = input('What do you want to name the new merged file? ')
	unifier.write(name)
	unifier.close()