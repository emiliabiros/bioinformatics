from Bio import Entrez


def get_sequence(genbank_id):
    Entrez.email = "emilia.biros@student.uj.edu.pl"

    handle = Entrez.efetch(
        db="nucleotide",
        id=genbank_id,
        rettype="fasta",
        retmode="text"
    )

    record = handle.read()
    handle.close()

    lines = record.strip().split("\n")
    sequence = "".join(line.strip() for line in lines if not line.startswith(">"))

    return sequence


def global_alignment(s, t, open_pen=10, ext_pen=1):
    n = len(s)
    m = len(t)

    NEG_INF = float("-inf")

    M = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
    X = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
    Y = [[NEG_INF] * (m + 1) for _ in range(n + 1)]

    M[0][0] = 0

    for i in range(1, n + 1):
        X[i][0] = -open_pen - (i - 1) * ext_pen

    for j in range(1, m + 1):
        Y[0][j] = -open_pen - (j - 1) * ext_pen

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            X[i][j] = max(
                M[i - 1][j] - open_pen,
                X[i - 1][j] - ext_pen,
                Y[i - 1][j] - open_pen
            )

            Y[i][j] = max(
                M[i][j - 1] - open_pen,
                Y[i][j - 1] - ext_pen,
                X[i][j - 1] - open_pen
            )

            if s[i - 1] == t[j - 1]:
                score = 5
            else:
                score = -4

            M[i][j] = max(
                M[i - 1][j - 1],
                X[i - 1][j - 1],
                Y[i - 1][j - 1]
            ) + score

    return max(
        M[n][m],
        X[n][m],
        Y[n][m]
    )


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

    genbank_id1, genbank_id2 = " ".join(lines).split()

    s = get_sequence(genbank_id1)
    t = get_sequence(genbank_id2)

    result = global_alignment(s, t)

    print(result)


if __name__ == "__main__":
    main()
