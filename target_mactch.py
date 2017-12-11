## Name :       Chenyu Su
## Course:      CST 205 Multimedia Desgin
## Project:     Primary Calculator
## Date:        12/10/2017
## Description: All my functions are cooperating with the primer function. The main function will ask user to input the target sequence,
##              and then pass to the find_target function. Then, the find_target function will taake the user's input as a parameter,
##              and check whether the target sequence whether appear in each sequence. If it does, the function will append the sequence
##              Id into a list, and returns. else, it will print "Target sequence is not in data base." as the answer. 
##              The calculation function just take the target sequence, and calculate the numbers of AT and GC. After the calculation finished
##              this function will return a list which only contains two numbers that refer to the numbers of AT and GC to the primer function.
## Note:        Jessie and Roberte made modifications to this code. It might not be the same as it was originally.

import csv, random, sys, string, locale
def seq_find(text):
    
    temp2 = find_target(text)
    return temp2


def find_target(target_seq):
    with open('seq_log.csv', 'r') as seq_log:
        keys = ['seq_ID', 'Sequence', 'Compliment']
        log_open = csv.DictReader(seq_log, fieldnames = keys)
        ID_list = []
        for line in log_open:
            temp_seq = line['Sequence']
            if(target_seq in temp_seq):

                
                ID_list.append(line['seq_ID'])
                ID_list.append(target_seq)
                return ID_list
        return "Target sequence is not in data base."

def calculation(target_seq):
    AT_counter = 0;
    GC_counter = 0;
    counter_list = [];
    for i in target_seq:
        if (i == 'A' or i == 'T'):
            AT_counter += 1
        else:
            GC_counter += 1
    counter_list.append(AT_counter)
    counter_list.append(GC_counter)
    
    return counter_list
                        
                
