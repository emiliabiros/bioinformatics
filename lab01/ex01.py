def count_dna_nucleotides(s):
  print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))


def main():
  s = input()
  count_dna_nucleotides(s)


if __name__ == "__main__":
  main()