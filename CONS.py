# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:26:06 2015

@author: ev
"""
seq1 = 'GATTACATAGACCA'
seq2 = 'TAGACCATAGACCA'
seq3 = 'ATACACATAGACCA'

dna = [seq1,seq2,seq3]

import numpy as np

dicti={}
for j in range(len(seq1)):
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
            
            
            
lis = np.zeros((4, len(seq1)))
#    

lis = np.array(lis)
bas = 'ACGT'

for j in range(len(bas)):
    for i in range(len(seq1)):
        lis[j][i]= dicti[str(i)][bas[j]]
        
for base,item in zip(bas,lis):
    print(base, '  :', item)
        
        
        
        
