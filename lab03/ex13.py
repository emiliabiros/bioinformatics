import sys
from Bio import Entrez


def count_genbank_entries(genus, start_date, end_date):
    Entrez.email = "emiliab@example.com"

    term = f'"{genus}"[Organism] AND ("{start_date}"[PDAT] : "{end_date}"[PDAT])'

    handle = Entrez.esearch(db="nucleotide", term=term)
    record = Entrez.read(handle)
    handle.close()

    return record["Count"]


def main():
    input_data = sys.stdin.read().splitlines()
    lines = [line.strip() for line in input_data if line.strip()]

    genus = lines[0]
    start_date = lines[1]
    end_date = lines[2]

    count_result = count_genbank_entries(genus, start_date, end_date)
    print(count_result)


if __name__ == "__main__":
    main()