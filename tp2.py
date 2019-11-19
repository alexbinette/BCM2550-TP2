import sys

try:
    file = sys.argv[1]
except (IOError, IndexError):
    error_message = """Error : Fasta sequence file missing at argv[1],
    please specify filepath"""
    print(error_message, file=sys.stderr)
    exit()

nuc_counter = 0
CG_counter = 0
seq = ""
with open(file, "r") as f:
    for line in f:
        if line[0] == ">":
            name, description = line.strip(">").split(" ")
            continue

        seq += line.rstrip("\n")

        for nuc in line:
            nuc_counter += 1

            if nuc == "C" or nuc == "G":
                CG_counter += 1

seq_rech = seq[100:130]
seq_rech_inv = ""
for nuc in seq_rech:
    if nuc == "C":
        seq_rech_inv += "G"
    if nuc == "G":
        seq_rech_inv += "C"
    if nuc == "A":
        seq_rech_inv += "T"
    if nuc == "T":
        seq_rech_inv += "A"

seq_rech_inv = seq_rech_inv[::-1]


prc_CG_counter = CG_counter/nuc_counter*100
print("The title of the sequence is {} and {}".format(name, description))
print("The sequence has {:,d} nucleotides".format(nuc_counter))
print("The GC content is {:.1f}%".format(prc_CG_counter))
print("The sequence from 100 to 130 is:\n{}".format(seq_rech))
print("""The reverse complement of
the sequence from 100 to 130 is:\n{}""".format(seq_rech_inv))
