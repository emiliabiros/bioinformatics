def dna_to_rna(t):
    t = t.replace("T", "U")
    print(t)


def main():
    t = input()
    dna_to_rna(t)


if __name__ == "__main__":
    main()