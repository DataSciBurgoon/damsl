# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:21:45 2016

@author: burgoonl
"""

import os, sys, glob
    

#filename = sys.argv[0]

#if there's only one SMI file then process it
#else, assume the files have already been processed
if len(glob.glob("*.smi")) == 1:
    filename = glob.glob("*.smi")
    f = open(filename[0], 'r')
    for line in f:
        chem_info = line.split("\t")
        chem_smiles = chem_info[0]
        chem_name = chem_info[1]
        fo_name = chem_name.rstrip() + ".smi"
        fo = open(fo_name, "w")
        line_to_write = chem_smiles + "\t" + chem_name + "\n"
        fo.write(line_to_write)
        fo.close()
    f.close()
    os.rename(filename[0], filename[0] + ".old")

