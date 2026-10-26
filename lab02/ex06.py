import sys


def parse_fasta(content):
    sequences = []
    current_seq = []

    for line in content.splitlines():
        line = line.strip()
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
    content = sys.stdin.read()
    dna_strings = parse_fasta(content)
    result = find_longest_common_substring(dna_strings)
    print(result)


if __name__ == "__main__":
    main()