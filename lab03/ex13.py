from Bio import Entrez


def count_genbank_entries(genus, start_date, end_date):
    Entrez.email = "emilia.biros@student.uj.edu.pl"

    handle = Entrez.esearch(
        db="nucleotide",
        term=f'"{genus}"[Organism]',
        mindate=start_date,
        maxdate=end_date,
        datetype="pdat",
    )

    record = Entrez.read(handle)
    handle.close()

    return record["Count"]


def main():
    lines = []
    while True:
        try:
            line = input()
            if not line.strip():
                if lines:
                    break
                continue
            lines.append(line.strip())
        except EOFError:
            break

    genus = lines[0]
    start_date = lines[1]
    end_date = lines[2]

    count_result = count_genbank_entries(genus, start_date, end_date)
    print(count_result)


if __name__ == "__main__":
    main()