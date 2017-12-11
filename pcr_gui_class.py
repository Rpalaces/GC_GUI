import csv, random, sys, string, locale
from target_mactch import find_target, calculation, seq_find

##File: pcr_gui_class.py
##Date:1/23/2017
##Author: Jesse V. Anacleto
##Class/Instr/TA: CST250 Multimedia/Biblarz/Crews
##Assignment:  CST Final Project
##Decription:  This file will contain the methods and variables I will use to create
##             a PCR(Polmerase Chain Reaction) Calculator - that is just a working title.  At first, we only wanted to
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
##             Both sequences will be added to a dictionary of DNA sequences that will be stored in a file.
##             2) The second feature I will add will allow the user to search the dictionary of DNA sequences to see if the
##             target DNA strand is present in any of them, and return/display a list of strands that possess the target sequence, represented by their unique key.
##             3) The third feature will allow the user to create and store a pair of primers that will be used assemble the target DNA sequence
##             There are guidelines for designing primers, so there will also need to be functions to check if the primers meet certain
##             conditions.
##             Example: They must end in either a G or a C, and they must have a GCPercentage of about 50% - 60%.


def check_gc_clamps(f_prim, r_prim):
    f_r_list =[]
    f_count = 0
    r_count = 0
    
    for i in range(len(f_prim)-1, len(f_prim) - 6, -1):  #Iterate backwards through the forward primer to check for a GC clamp in the 3' end.
        if f_prim[i] == 'G' or f_prim[i] == 'C':
            f_count += 1
    f_r_list.append(f_count)
    for i in range(0, 5):   #The reverse primer is already arranged with the 3' end on the left.  
        if r_prim[i] == 'G' or r_prim[i] == 'C':
            r_count += 1
    f_r_list.append(r_count)
    return f_r_list

def calc_tm(AT_count, GC_count):  ##Tm = 2 °C(A + T) + 4 °C(G + C) = °C Tm <--- Only accurate for short DNA sequences.
    tm = 2*(AT_count) + 4*(GC_count)
    return tm

def test_primer(prim_list):
    if (prim_list[0][2] < 50.0 or prim_list[0][2] > 60.0) or (prim_list[1][2] < 50.0 or prim_list[1][2] > 60.0):
        print("GC %")
        return False
    elif (prim_list[0][3] == 0) or (prim_list[1][3] == 0):
        print("GC clamp")
        return False
    elif (prim_list[0][4] >= 65) or (prim_list[1][3] >= 65):
        print("TM")
        return False
    return True
            
def primer(seq):
    
    primer_list = []
    for_prim_data = []
    rev_prim_data = []
    for_prim = ''
    rev_prim = ''
    targ_seq = seq

    #print(len(targ_seq[1]))
    
    for i in range(0, 20):   ##build a max length forward primer.
        for_prim += targ_seq[1][i]

    for i in range(len(targ_seq[1]) - 1, len(targ_seq[1]) - 21, - 1):  ##build a reverse primer at max length
        rev_prim = targ_seq[1][i] + rev_prim
        
    rev_prim = get_compliment(rev_prim)  ##Start filling in primer_list elements
    for_prim_data.append(for_prim)
    rev_prim_data.append(rev_prim)
    for_prim_data.append(len(for_prim))
    rev_prim_data.append(len(rev_prim))
    fgc_cont = (100/len(for_prim))*(calculation(for_prim)[1])  ## Calculate GC% - Daniel was right ... one line of code.
    for_prim_data.append(fgc_cont)
    rgc_cont = (100/len(rev_prim))*(calculation(rev_prim)[1])
    rev_prim_data.append(rgc_cont)
    gc_clamp = check_gc_clamps(for_prim, rev_prim)  ## check the 3' ends of the primers for GC clamps.
    for_prim_data.append(gc_clamp[0])
    rev_prim_data.append(gc_clamp[1])
    ftm = calc_tm(calculation(for_prim)[0], calculation(for_prim)[1])
    rtm = calc_tm(calculation(rev_prim)[0], calculation(rev_prim)[1])
    for_prim_data.append(ftm)
    rev_prim_data.append(rtm)
    primer_list.append(for_prim_data)
    primer_list.append(rev_prim_data)
    
    if test_primer(primer_list) == False:
        return False
    #print (primer_list[0][0])
    return primer_list
    
    
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
        
def get_sequence(seq_id):
    with open('seq_log.csv', 'r') as seq_log:
        keys = ['seq_ID', 'Sequence', 'Compliment']
        log_open = csv.DictReader(seq_log, fieldnames = keys)
        for line in log_open:
            if line['seq_ID'] == seq_id:
                return line['Sequence'], line['Compliment']
                
#def get_sequence_ID(targ_seq):
    #with open('seq_log.csv', 'r') as seq_log:
        #keys = ['seq_ID', 'Sequence', 'Compliment']
        #log_open = csv.DictReader(seq_log, fieldnames = keys)
        #for line in log_open:
            #if line['Sequence'] == targ_seq:
                #return line['seq_ID']
    
def print_seq_log():
    with open("seq_log.csv", "r") as csv_file:
        log_dict = csv.DictReader(csv_file)

        for line in log_dict:
            print(line)
    csv_file.close()

def get_compliment(sequence):
    length = len(sequence)
    seq_comp = ''
    for i in range(0, length):
        if sequence[i] == 'A':
            seq_comp += 'T'
        elif sequence[i] == 'T':
            seq_comp += 'A'
        elif sequence[i] == 'G':
            seq_comp += 'C'
        elif sequence[i] == 'C':
            seq_comp += 'G'
    return seq_comp

def generate_rand_dna_seq():   #We used this to populate our data base.
    length = get_kbp_size()
    nucleic_acids = "ATGC"
    seq = ''
    seq_comp = ''
    seq_id = rand_seq_key()
    
    for i in range(0, length):
        seq += nucleic_acids[random.randint(0, 3)]

    seq_comp = get_compliment(seq)
    
    with open("seq_log.csv", "a") as csv_file:
        keys = ['seq_ID', 'Sequence', 'Compliment']
        log_file = csv.DictWriter(csv_file, fieldnames = keys)
        log_file.writerow({'seq_ID' : seq_id, 'Sequence' : seq, 'Compliment' : seq_comp})
        print(seq)
        print(seq_comp)
    ##csv_file.close()
    


##generate_rand_dna_seq()
##print_seq_log()
##print("Get seq_ID returns = ", get_sequence('seq1R'))



    
