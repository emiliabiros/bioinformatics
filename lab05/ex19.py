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


def semiglobal_alignment(s, t):
    n = len(s)
    m = len(t)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    trace = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        trace[i][0] = "U"

    for j in range(1, m + 1):
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

    best_score = float("-inf")
    end_i = n
    end_j = m

    for j in range(m + 1):
        if dp[n][j] > best_score:
            best_score = dp[n][j]
            end_i = n
            end_j = j

    for i in range(n + 1):
        if dp[i][m] > best_score:
            best_score = dp[i][m]
            end_i = i
            end_j = m

    i = end_i
    j = end_j

    align_s = []
    align_t = []

    while i > 0 and j > 0:
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

    while i > 0:
        align_s.append(s[i - 1])
        align_t.append("-")
        i -= 1

    while j > 0:
        align_s.append("-")
        align_t.append(t[j - 1])
        j -= 1

    align_s = list(reversed(align_s))
    align_t = list(reversed(align_t))

    align_s.extend(list(s[end_i:]))
    align_t.extend(["-"] * (n - end_i))

    align_s.extend(["-"] * (m - end_j))
    align_t.extend(list(t[end_j:]))

    return best_score, "".join(align_s), "".join(align_t)


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

    score, aligned_s, aligned_t = semiglobal_alignment(s, t)

    print(score)
    print(aligned_s)
    print(aligned_t)


if __name__ == "__main__":
    main()