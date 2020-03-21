from pathlib import Path

def seq_ping():
    print("OK")


def seq_read_fasta(filename):

    file_contents = Path(filename).read_text().split("\n")[1:]
    seq = Path(filename).join(contents)
    return seq

#Read a file with a DNA sequence in FASTA format
#eliminates the head part to leave only the body part
#eliminate blank spaces
#return the body part as a string

def seq_len(seq):
    length=len(seq)
    return(length)

def seq_count_base(seq, base):
    counter= 0
    for element in seq:
        if element == base:
            count = counter + 1
    return counter

