#program to check if the sequence is RNA or DNA

seq1 = 'ACGAUGA'
seq2 = 'TACATGC'
DNA = 'ATCG'
RNA =  'AUCG'

#creating a funciton for validation

def validation(seq, seqtype):
	for n in seq:
		if n not in seqtype:
			return False
	return True

#calling the function to check the sequences we have

print(validation(seq1,RNA))
print(validation(seq2,DNA))
