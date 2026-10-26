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


def find_overlap_edges(fasta_dict):
    edges = []
    ids = list(fasta_dict.keys())

    for i in range(len(ids)):
        for j in range(len(ids)):
            if i == j:
                continue

            id_s = ids[i]
            id_t = ids[j]

            s = fasta_dict[id_s]
            t = fasta_dict[id_t]

            suffix_s = s[-3:]
            prefix_t = t[:3]

            if suffix_s == prefix_t:
                edges.append((id_s, id_t))

    return edges


def main():
    content = sys.stdin.read()
    fasta_dict = parse_fasta_with_ids(content)
    edges = find_overlap_edges(fasta_dict)

    for edge in edges:
        print(f"{edge[0]} {edge[1]}")


if __name__ == "__main__":
    main()