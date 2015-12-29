# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:54:51 2015

@author: evgeniydonev
"""
#This code import a FASTA file and gives the name and the sequence

def read_FASTA(filename):
    """Dealing with only one sequence per file"""
    fh = open(filename)
    myfile = fh.read() #myfile is a string
    name = myfile.split('\n')[0][1:]          #getting the first line 
    sequence = ''.join(myfile.split('\n')[1:])  #getting from the second line 
    print("The name is: %s"%name)
    print("The sequence is: %s"%sequence)
    fh.close()
    return name,sequence


def read_many_FASTA_sequences(filename):
    """If we have many FASTA sequences in one file this function is more convenient"""
    sequence_list = []
    with open(filename) as fil:
        contents = fil.read()            # reading all the sequences
    entries = contents.split('>')[1:]     # split the file at '>' and skip blank first entry
    for myfile in entries:
        name = myfile.split('\n')[0]
        sequence = ''.join(myfile.split('\n')[1:])
        #print("The name is: %s"%name)
        #print("The sequence is: %s"%sequence)
        sequence_list.append(sequence)
    return sequence_list

#Now we are importing the FASTA file from the course web
#We save it as a FASTA ('myfasta.fasta') file on our local machine and import it from there

if __name__ == "__main__":
    print('\n')
    file = 'myfasta.fasta'  
    read_FASTA(file)
    print('\n\n')
    read_many_FASTA_sequences(file)
     


# Nice work, a bit more than required for the task. :-) /Uwe


    
