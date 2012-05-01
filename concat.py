import os #we need this.
#path = 'Level_3\/'
path = 'myTest\/'

def concat(path,output): #takes a path and an output, e.g. concat('Level_3\/','test') would look in Level_3/ for files and output to 'test.tab'
    results = open(output+'.tab','w') #our output file
    listing = os.listdir(path) #the directory with all of the patient data files
    all_files=[] #list of the contents of every file
    for infile in listing: #so for each file in our directory
        cur_file = open(path+infile).readlines() #read that file
        del cur_file[0] #get rid of its headers
        all_files.append(cur_file) #and add its contents to the list of all files.

    genes = [] #need our gene IDs for the header, this wil be a list of them
    for line in all_files[0]: #just going through the first file because gene IDs should be the same for everything.
        line = line.strip('\n').split('\t')
        genes.append(line[1]) #adding each gene ID to our list.
        
    #setting up header
    results.write('barcode\t') #our patient ID (PID)
    for gene in genes: #so for each gene ID in our genes
        results.write(gene+'\t') #we write it and then a tab. this is a tab delimited file, you will see tabs frequently.
    results.write('\n')
    results.write('d\t')
    for gene in genes: #same concept as above but with 'c' for continuous variable.
        results.write('c\t')
    results.write('\n')
    results.write('\t')
    for gene in genes: #and again, but just tabs because we don't have a class variable.
        results.write('\t')
    results.write('\n')

    #get gene values and PID for each file, then write to output file.
    for file_contents in all_files: 
        gene_vals=[] #a list to hold our gene values for each file
        PID = file_contents[0].split('\t')[0] #Just taking the PID from the first line of each file.
        for line in file_contents:
            line = line.strip('\n').split('\t') #turns the string into a list, split at tabs. (removed return character)
            gene_vals.append(str(line[2])+'\t') #amassing gene values into a list.
        if len(gene_vals) != len(genes): #gives and error if there aren't as many gene_vals as gene IDs.
                print 'error!'
        gene_vals = ''.join(gene_vals) #joining out list of "geneval\t"'s into a giant string
        results.write(str(PID)+'\t'+gene_vals+'\n') #what actually writes to file.
    results.close() #don't leave files open.

   

    
