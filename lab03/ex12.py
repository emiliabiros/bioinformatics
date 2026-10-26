from Bio import Entrez, SeqIO


def get_shortest_fasta(genbank_ids):
    Entrez.email = "emilia.biros@student.uj.edu.pl"

    handle = Entrez.efetch(
        db="nucleotide",
        id=",".join(genbank_ids),
        rettype="fasta",
        retmode="text",
    )

    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()

    if not records:
        return ""

    shortest_record = min(records, key=lambda r: len(r.seq))

    return shortest_record.format("fasta").strip()


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

    genbank_ids = " ".join(lines).split()
    result = get_shortest_fasta(genbank_ids)
    print(result)


if __name__ == "__main__":
    main()