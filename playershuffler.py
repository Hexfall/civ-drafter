from sys import argv
from random import shuffle

def main():
    l = argv[1:]
    shuffle(l)

    print("\n".join(l))

if __name__ == "__main__":
    main()
