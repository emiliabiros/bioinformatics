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


def fitting_alignment(s, t):
    n = len(s)
    m = len(t)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    trace = [[None] * (m + 1) for _ in range(n + 1)]

    for j in range(1, m + 1):
        dp[0][j] = -j
        trace[0][j] = "L"

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = 1 if s[i - 1] == t[j - 1] else -1

            candidates = [
                (dp[i - 1][j - 1] + match, "D"),
                (dp[i - 1][j] - 1, "U"),
                (dp[i][j - 1] - 1, "L")
            ]

            dp[i][j], trace[i][j] = max(candidates, key=lambda x: x[0])

    end_i = max(range(n + 1), key=lambda i: dp[i][m])
    score = dp[end_i][m]

    i = end_i
    j = m

    align_s = []
    align_t = []

    while j > 0:
        direction = trace[i][j]

        if direction == "D":
            align_s.append(s[i - 1])
            align_t.append(t[j - 1])
            i -= 1
            j -= 1

        elif direction == "U":
            align_s.append(s[i - 1])
            align_t.append("-")
            i -= 1

        elif direction == "L":
            align_s.append("-")
            align_t.append(t[j - 1])
            j -= 1

    return score, "".join(reversed(align_s)), "".join(reversed(align_t))


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

    score, aligned_s, aligned_t = fitting_alignment(s, t)

    print(score)
    print(aligned_s)
    print(aligned_t)


if __name__ == "__main__":
    main()