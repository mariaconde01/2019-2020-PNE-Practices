from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
   file_contents = Path(filename).read_text()
   file = file_contents.split('\n')
   body = "".join(file[1:])
   return(body)

#Read a file with a DNA sequence in FASTA format
#eliminates the head part to leave only the body part
#eliminate blank spaces
#return the body part as a string

def seq_len(seq):
        counter = 0
        for element in seq:
            counter += 1
        return counter

def seq_count_base(seq, base):
    counter= 0
    for element in seq:
        if element == base:
            counter+=1
    return counter

def seq_count(seq):

    dictionary = {'A': seq_count_base(seq, 'A'), 'T': seq_count_base(seq, 'T'), 'C': seq_count_base(seq, 'C'),
           'G': seq_count_base(seq, 'G')}

    return dictionary

def seq_reverse (seq):

    return seq[::-1]

def seq_complement (seq):

    bases={'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_bases = ""
    for element in seq:
        comp_bases += bases[element]
    return comp_bases

def processing_genes(seq):

    dict_base= seq_count(seq)
    max_base= max(dict_base, key=dict_base.get) #la funcion get te encuentra la base mas frecuente
    return max_base