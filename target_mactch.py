
import csv, random, sys, string, locale

# Asking user to input the target sequence, and then pass to the find_target function
def main():
    temp = input("What is your target sequence? ")
    temp2 = find_target(temp)
    ##print(f"IDs that contain your target sequence are in the list : {temp2[0]}")
    return temp2

# this function will taake the user's input as a parameter, and check whether the target sequence whether appear in each sequence.
# If it does, the function will append the sequence Id into a list, and returns.
# else, it will print Target sequence is not in data base."
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
    
# This function just take the target sequence, calculate the numbers of AT and GC.
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
