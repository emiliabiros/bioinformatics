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


def global_alignment(s, t):
    n = len(s)
    m = len(t)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = -i

    for j in range(1, m + 1):
        dp[0][j] = -j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score = 1 if s[i - 1] == t[j - 1] else -1

            dp[i][j] = max(
                dp[i - 1][j - 1] + score,
                dp[i - 1][j] - 1,
                dp[i][j - 1] - 1
            )

    return dp


def isolating_symbols(s, t):
    forward = global_alignment(s, t)
    backward = global_alignment(s[::-1], t[::-1])

    n = len(s)
    m = len(t)

    total = 0

    for i in range(n):
        for j in range(m):
            score = 1 if s[i] == t[j] else -1

            total += (
                forward[i][j]
                + score
                + backward[n - i - 1][m - j - 1]
            )

    return forward[n][m], total


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

    score, total = isolating_symbols(s, t)

    print(score)
    print(total)


if __name__ == "__main__":
    main()