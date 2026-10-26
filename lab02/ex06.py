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


def find_longest_common_substring(dna_strings):
    if not dna_strings:
        return ""

    shortest = min(dna_strings, key=len)
    n = len(shortest)

    for length in range(n, 0, -1):
        for i in range(n - length + 1):
            sub = shortest[i : i + length]
            if all(sub in dna for dna in dna_strings):
                return sub

    return ""


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

    dna_strings = parse_fasta(lines)
    result = find_longest_common_substring(dna_strings)
    print(result)


if __name__ == "__main__":
    main()