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


def maximizing_gaps(s, t):
    n = len(s)
    m = len(t)

    dp = [[(0, 0)] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = (0, i)

    for j in range(1, m + 1):
        dp[0][j] = (0, j)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score = 1 if s[i - 1] == t[j - 1] else -1

            candidates = [
                (dp[i - 1][j - 1][0] + score, dp[i - 1][j - 1][1]),
                (dp[i - 1][j][0], dp[i - 1][j][1] + 1),
                (dp[i][j - 1][0], dp[i][j - 1][1] + 1)
            ]

            dp[i][j] = max(candidates)

    return dp[n][m][1]


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

    sequences = parse_fasta(lines)

    s = sequences[0]
    t = sequences[1]

    result = maximizing_gaps(s, t)

    print(result)


if __name__ == "__main__":
    main()