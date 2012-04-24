#bioinformatic file management functions to be implemented
import sys

#goals
	#take multiple files and merge them into single data table
	#be able to transpose matrix(switching from samples to genes as entries)
	#be able to deal with FASTA formats(WHY DOESNT ORANGE DO THIS?)
	
	
	

#fasta reader
def fastaReader(fastaFile)

	pass



def transposeMatrix(textfile)	#what structure to use for matrix? array?  npArray?  nested lists?
	file = open(textfile, 'r')
	file2 = open(textfile, 'w')
	for c in zip(*(l.split() for l in file.readlines() if l.strip())):
	    file2.write(' '.join(c))
	return file2


def concatFiles() #should arguments be directory, list of files, or allow either

	pass
