import csv, random, sys, string, locale
from PIL import Image
from PyQt5.QtWidgets import (QApplication, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QComboBox, QLabel)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
##File: pcr_gui_class.py
##Date:1/23/2017
##Author: Jesse V. Anacleto
##Class/Instr/TA: CST250 Multimedia/Biblarz/Crews
##Assignment:  CST Final Project
##Decription:  This file will contain the methods and variables I will use to create
##             a PCR(Polmer Chain Reaction) Calculator - that is just a working title.  At first, we only wanted to
##             calculate a GC Percentage, but there are many more relevant calculations
##             we can make and present visually.  This is primarily a tool for education,
##             one I wanted to work on to help increase my own understanding of the  basic PCR process.
##             Example:  In Physics 101 we learn to make basic calcuations while omitting signifact variables, like wind resistance and drag.
##             This tool will also makes a limited set of calculations based on introductory ideas.  
##             1) The first feature I am trying to add are functions to generate a random DNA sequence
##             between .001kbp and 10 kbp (Kilo Base Pairs are the unit of measure for the length of a DNA sequence
##             if my understanding is correct) - That's all just fancy talk for 1 - 10,000 base pairs.  The function will automatically
##             generate the sequence's compliment, which will be necessary for designing the primers (the oligonucleotide components - short DNA strands)
##             that guide the assembly of the target DNA sequence (the portion of the original DNA sequence we wish to amplify (replicate, copy, etc).
##             Both sequences will be added to a dictionary of DNA sequnces that will be stored in a file.
##             2) The second feature I will add will allow the user to search the dictionary of DNA sequences to see if the
##             target DNA strand is present in any of them, and return/display a list of strands that possess the target sequence, represented by their unique key.
##             3) The third feature will allow the user to create and store a pair of primers that will be used assemble the target DNA sequence
##             There are guidelines for designing primers, so there will also need to be functions to check if the primers meet certain
##             conditions.
##             Example: they must end in either a G or a C, and they must have a GCPercentage of about 50% - 60%.

##num_sequences = 0

def get_kbp_size():
    kbp_size = int(input("Enter kbp value: "))
    return kbp_size
    
def rand_seq_key():
    with open('num_seq.txt', 'r') as num_txt:
        temp = num_txt.read()
        temp = int(temp)
        num_sequences = temp
        num_sequences = num_sequences + 1
    with open('num_seq.txt', 'w') as num_txt:
        num_txt.write(f'{num_sequences}')
        return "seq" + f'{num_sequences}' + "R"
        
def get_sequence(seq_id, targ_seq):
    with open('seq_log.csv', 'r') as seq_log:
        keys = ['seq_ID', 'Sequence', 'Compliment']
        log_open = csv.DictReader(seq_log, fieldnames = keys)
        for line in log_open:
            if line['seq_ID'] == seq_id:
                return line['Sequence'], line['Compliment']
    
    
        
def print_seq_log():
    with open("seq_log.csv", "r") as csv_file:
        log_dict = csv.DictReader(csv_file)

        for line in log_dict:
            print(line)
    csv_file.close()
        
def generate_rand_dna_seq():
    length = get_kbp_size()
    nucleic_acids = "ATGC"
    seq = ''
    seq_comp = ''
    seq_id = rand_seq_key()
    
    for i in range(0, length):
        seq += nucleic_acids[random.randint(0, 3)]
        if seq[i] == "A":
            seq_comp += "T"
        elif seq[i] == "T":
            seq_comp += "A"
        elif seq[i] == "G":
            seq_comp += "C"
        elif seq[i] == "C":
            seq_comp += "G"
    
    with open("seq_log.csv", "a") as csv_file:
        keys = ['seq_ID', 'Sequence', 'Compliment']
        log_file = csv.DictWriter(csv_file, fieldnames = keys)
        log_file.writerow({'seq_ID' : seq_id, 'Sequence' : seq, 'Compliment' : seq_comp})
        print(seq)
        print(seq_comp)
    csv_file.close()
    


generate_rand_dna_seq()
print_seq_log()
print("Get sequence returns = ", get_sequence('seq20R', ''))



    
