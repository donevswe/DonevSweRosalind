# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:26:06 2015

@author: ev
"""
from ReadFasta import read_many_FASTA_sequences


file = 'CONS.fasta'

dna = read_many_FASTA_sequences(file)

import numpy as np

dicti={}
for j in range(len(dna[0])):
    dicti[str(j)]={}
    for item in 'ATGC':
        dicti[str(j)][item] = 0
    
    



for seq in dna:
    for i in range(len(seq)):
        if seq[i] == 'A':
            dicti[str(i)]['A'] +=1
           
            
        elif seq[i] == 'T':
            dicti[str(i)]['T'] +=1
            
        elif seq[i] == 'G':
            dicti[str(i)]['G'] +=1
            
        elif seq[i] == 'C':
            dicti[str(i)]['C'] +=1
            
            
            
lis = np.zeros((4, len(dna[0])))
#    

lis = np.array(lis)
bas = 'ACGT'

profile = [0]*len(dna[0])
profile_bas = [0]*len(dna[0])
for j in range(len(bas)):
    for i in range(len(dna[0])):
        lis[j][i]= int(dicti[str(i)][bas[j]])
        if lis[j][i] > profile[i]:
            profile[i] = lis[j][i]
            profile_bas[i] = bas[j]
            
print(''.join(str(b) for b in profile_bas))        
for base,item in zip(bas,lis):
    print(base, ': ', ' '.join(str(int(e)) for e in item))
        
        
        
        
