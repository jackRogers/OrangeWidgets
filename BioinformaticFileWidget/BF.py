#bioinformatic file management functions to be implemented
import sys

#goals
    #take multiple files and merge them into single data table
    #be able to transpose matrix(switching from samples to genes as entries)
    #be able to deal with FASTA formats(WHY DOESNT ORANGE DO THIS?)

import os





#fasta reader
def fastaReader(fastaFile):

    pass



def transposeMatrix(textfile):  #what structure to use for matrix? array?  npArray?  nested lists?
    file = open(textfile, 'r')
    file2 = open(textfile, 'w')
    for c in zip(*(l.split() for l in file.readlines() if l.strip())):
        file2.write(' '.join(c))
    return file2


def concatFiles(path): #should arguments be directory

    #initialize dictionary
    dataDict = {}

    #get list of files
    fileList = os.listdir(path)

    #for each file in file list
    for f in fileList:

        #open file
        fh = open(os.path.join(path,f),'r')

        #skip header
        header = fh.readline()

        #grab first line
        firstLine = fh.readline().strip("\n").split("\t")

        #intialize dictionary for paitient by paitient id
        dataDict[firstLine[0]] = {}

        #add first gene from first line
        dataDict[firstLine[0]][firstLine[1]] = firstLine[2]

        #for rest of lines
        for i in fh.readlines():
            line = i.strip("\n").split("\t")
            dataDict[line[0]][line[1]] = line[2]

    return dataDict


def makeDataFile(newFileName,dataDict):
	fh = open(newFileName,'w')
	paitients = dataDict.keys()
	genes = dataDict[paitients[0]].keys()
	
	header = "paitientID\t"
	for g in genes:
		header += g
		header += "\t"
	header += "value\n"
	
	fh.write(header)
	
	shitz = "d\t"
	for i in range(len(genes)):
		shitz += "c\t"
	shitz += "\n"
	
	fh.write(shitz)
		
	for p in paitients:
		line = p
		line += "\t"
		for g in genes:
			line += dataDict[p][g]
			line += "\t"
		line += "\n"
		fh.write(line)
	fh.close
		
		 
	
