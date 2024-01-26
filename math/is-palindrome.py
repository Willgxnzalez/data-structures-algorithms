

def isPalindromeString(x: int) -> bool:
    strx = str(x)
    return strx == strx[::-1]


def isPalindromeNoString(x: int) -> bool:
    if x < 0: return False
    num = []
    while x > 0:
        num.append(x % 10)
        x //= 10
    return num == num[::-1]


def main():
    print(isPalindromeString(121))
    print(isPalindromeString(-747))
    print(isPalindromeNoString(121))
    print(isPalindromeNoString(-747))

if __name__ == "__main__":
    main()