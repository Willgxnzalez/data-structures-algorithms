import math
p_one = 2/3

p_two = 1-p_one

entropy = -(p_one * math.log2(p_one) + p_two * math.log2(p_two))

print(f"Entropy of {p_one:.2f}:", entropy)