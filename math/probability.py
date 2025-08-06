import random

def main():
    for length in (10, 100, 1000, 10000, 1000000, 10000000):
        outcomes = [random.randint(0,1) for _ in range(length)]
        print(f"probability of true with length {length}:", sum(outcomes)/length)

if __name__ == "__main__":
    main()