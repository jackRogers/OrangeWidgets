#bioinformatic file management functions to be implemented

#goals
    #take multiple files and merge them into single data table
    #be able to transpose matrix(switching from samples to genes as entries)
    #be able to deal with FASTA formats(WHY DOESNT ORANGE DO THIS?)

"""
IMPORTS
"""
import os
import sys
import csv

"""
GLOBALS
"""
EXAMPLEFILELIST=['breast-cancer-wisconsin.tab', 'breast-cancer-wisconsin-cont.tab']


"""
SCRIPT
"""

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
	
	header = "patientID\t"
	#add class label
	for g in genes:
		header += g
		header += "\t"
	header += "value\n"
	
	fh.write(header)
	
	shitz = "d\t"
	#add class label as discrete
	for i in range(len(genes)):
		shitz += "c\t"
	shitz += "\n"
	
	fh.write(shitz)
	
	
	
		
	for p in patients:
		line = p
		line += "\t"
		for g in genes:
			line += dataDict[p][g]
			line += "\t"
		line += "\n"
		fh.write(line)
	fh.close
	
def makeCSVDataFile(newFileName,dataDict,label):
	fh = open(newFileName,'w')
	writer = csv.writer(fh,delimiter = "\t")
	patients = dataDict.keys()
	genes = dataDict[patients[0]].keys()
	
	header = []
	header.append("patientID")
	#add class label
	header.append("type")
	for g in genes:
		header.append(g)
	
	writer.writerow(header)
	
	header2 = []
	header2.append('d')
	#make class label discrete
	header2.append('d')
	for g in genes:
		header2.append('c')
	
	writer.writerow(header2)
	
	#make second column class label, get all other \t's
	header3 = []
	header3.append('')
	header3.append('class')
	for g in genes:
		header3.append('')
	
	
	for p in patients:
		line = []
		line.append(p)
		line.append(label)
		for g in genes:
			line.append(dataDict[p][g])
		writer.writerow(line)
		
	fh.close
	
	