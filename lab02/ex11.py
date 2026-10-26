def find_motif_locations(s, t):
    locations = []
    len_s = len(s)
    len_t = len(t)

    for i in range(len_s - len_t + 1):
        if s[i : i + len_t] == t:
            locations.append(i + 1)

    return locations


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

    s = lines[0]
    t = lines[1]

    locations = find_motif_locations(s, t)

    print(*locations)


if __name__ == "__main__":
    main()