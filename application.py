from genome_toolkit import genomeToolkit

gt = genomeToolkit()

seq = "AATTTTAAAAC"
kmer = "AA"
k_len = 3

print(f'Sequence: {seq}')
print(f'k-mer: {kmer}')
print(f'Repeats found: {gt.count_kmer(seq, kmer)}')
print(f'Most frequent k-mer: {gt.find_most_frequent_kmers(seq, k_len)}')
