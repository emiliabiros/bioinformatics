def parse_fasta(lines):
    sequences = []
    current_seq = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current_seq:
                sequences.append("".join(current_seq))
                current_seq = []
        else:
            current_seq.append(line)

    if current_seq:
        sequences.append("".join(current_seq))

    return sequences


def reverse_complement(s):
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complements[char] for char in reversed(s))


def get_orf_proteins(dna):
    codon_table = {
        "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
        "TAT": "Y", "TAC": "Y", "TAA": "Stop", "TAG": "Stop",
        "TGT": "C", "TGC": "C", "TGA": "Stop", "TGG": "W",
        "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    proteins = set()
    strands = [dna, reverse_complement(dna)]

    for strand in strands:
        for frame in range(3):
            codons = [strand[i:i+3] for i in range(frame, len(strand) - 2, 3)]

            for i in range(len(codons)):
                if codons[i] == "ATG":
                    current_protein = []
                    found_stop = False

                    for j in range(i, len(codons)):
                        c = codons[j]
                        aa = codon_table.get(c, "")
                        if aa == "Stop":
                            found_stop = True
                            break
                        current_protein.append(aa)

                    if found_stop:
                        proteins.add("".join(current_protein))

    return proteins


def main():
    lines = []
    while True:
        try:
            line = input()
            if not line.strip():
                if lines:
                    break
                continue
            lines.append(line)
        except EOFError:
            break

    sequences = parse_fasta(lines)

    dna = sequences[0]
    unique_proteins = get_orf_proteins(dna)

    for protein in unique_proteins:
        print(protein)


if __name__ == "__main__":
    main()