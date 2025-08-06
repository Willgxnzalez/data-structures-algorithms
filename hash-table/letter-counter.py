from collections import defaultdict

def count_letters(words):
    freq = defaultdict(int)
    
    for word in words:
        for c in word.lower():
            freq[c] += 1
    return dict(freq)

if __name__ == "__main__":
    names = ["Allie", "Camden", "Charley", "Cole", "Georgia", "Goldie", "James", "Nolan", "Poopy", "Raddix", "Ricky", "Weston"]
    print(count_letters(names))