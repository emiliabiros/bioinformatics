import sys


def parse_fasta_with_ids(content):
    fasta_dict = {}
    current_id = None
    current_seq = []

    for line in content.splitlines():
        line = line.strip()
        if line.startswith(">"):
            if current_id:
                fasta_dict[current_id] = "".join(current_seq)
                current_seq = []
            current_id = line[1:].strip()
        else:
            current_seq.append(line)

    if current_id:
        fasta_dict[current_id] = "".join(current_seq)

    return fasta_dict


def calculate_gc_content(dna):
    gc_count = dna.count("C") + dna.count("G")

    return (gc_count / len(dna)) * 100


def find_highest_gc(fasta_dict):
    max_gc = -1.0
    best_id = ""

    for seq_id, dna in fasta_dict.items():
        gc = calculate_gc_content(dna)
        if gc > max_gc:
            max_gc = gc
            best_id = seq_id

    return best_id, max_gc


def main():
    content = sys.stdin.read()
    fasta_dict = parse_fasta_with_ids(content)

    best_id, max_gc = find_highest_gc(fasta_dict)

    print(best_id)
    print(max_gc)


if __name__ == "__main__":
    main()