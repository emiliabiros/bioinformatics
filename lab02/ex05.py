def hamming_distance(s, t):
    diff = 0

    for i in range (len(s)):
        if s[i] != t[i]:
            diff += 1

    print(diff)


def main():
    s = input()
    t = input()
    hamming_distance(s, t)


if __name__ == "__main__":
    main()