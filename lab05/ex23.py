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


def edit_distance(s, t, limit=3):
    n = len(s)
    m = len(t)

    if abs(n - m) > limit:
        return limit + 1

    dp = [[limit + 1] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(max(1, i - limit), min(m, i + limit) + 1):
            cost = 0 if s[i - 1] == t[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[n][m]


def find_pattern(s, t):
    for i in range(len(s) - 34):
        sub_s = s[i:i + 35]
        for j in range(len(t) - 34):
            sub_t = t[j:j + 35]
            if sum(a != b for a, b in zip(sub_s, sub_t)) <= 10:
                if edit_distance(sub_s, sub_t) <= 3:
                    return sub_s
    return ""


def count_pattern(seq, pattern):
    count = 0
    i = 0
    while i <= len(seq) - 35:
        if edit_distance(seq[i:i + 35], pattern) <= 3:
            count += 1
            i += 35
        else:
            i += 1
    return count


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

    pattern = find_pattern(s, t)
    result1 = count_pattern(s, pattern)
    result2 = count_pattern(t, pattern)

    print(result1, result2)


if __name__ == "__main__":
    main()