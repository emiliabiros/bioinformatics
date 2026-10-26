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


def transition_transversion_ratio(s1, s2):
    purines = {"A", "G"}
    pyrimidines = {"C", "T"}

    transitions = 0
    transversions = 0

    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            if (char1 in purines and char2 in purines) or (char1 in pyrimidines and char2 in pyrimidines):
                transitions += 1
            else:
                transversions += 1

    if transversions == 0:
        return float(transitions)

    return transitions / transversions


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

    s1 = sequences[0]
    s2 = sequences[1]

    result = transition_transversion_ratio(s1, s2)
    print(result)


if __name__ == "__main__":
    main()