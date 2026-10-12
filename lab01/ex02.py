def complement_strand_dna(s):
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}

    reverse_complement = ""

    for c in reversed(s):
        reverse_complement += complements[c]

    print(reverse_complement)


def main():
    s = input()
    complement_strand_dna(s)


if __name__ == "__main__":
    main()