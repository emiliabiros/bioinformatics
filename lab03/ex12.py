import sys
from Bio import Entrez, SeqIO


def get_shortest_fasta(genbank_ids):
    Entrez.email = "emilia.biros@student.uj.edu.pl"

    handle = Entrez.efetch(
        db="nucleotide", id=",".join(genbank_ids), rettype="fasta", retmode="text"
    )

    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()

    if not records:
        return ""

    shortest_record = min(records, key=lambda r: len(r.seq))

    fasta_output = f">{shortest_record.description}\n{str(shortest_record.seq)}"
    return fasta_output


def main():
    input_data = sys.stdin.read().strip()

    genbank_ids = input_data.split()

    result = get_shortest_fasta(genbank_ids)
    print(result)


if __name__ == "__main__":
    main()