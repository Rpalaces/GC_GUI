
import csv, random, sys, string, locale
def seq_find(text):
    
    temp2 = find_target(text)
    ##print(f"IDs that contain your target sequence are in the list : {temp2[0]}")
    return temp2


def find_target(target_seq):
    with open('seq_log.csv', 'r') as seq_log:
        keys = ['seq_ID', 'Sequence', 'Compliment']
        log_open = csv.DictReader(seq_log, fieldnames = keys)
        ID_list = []
        for line in log_open:
            temp_seq = line['Sequence']
            if(target_seq in temp_seq):

                ##print(f"Your target sequence oppears in {line['seq_ID']} at index {temp_seq.find(target_seq)}.")
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
                        
                
