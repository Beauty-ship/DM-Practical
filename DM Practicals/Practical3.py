from itertools import permutations, product

# Input
digits = input("Enter digits (no space, e.g. 123): ")

# Convert to list
digits_list = list(digits)

# Length of permutation
r = int(input("Enter length of permutation: "))

# -----------------------------
# Without Repetition
# -----------------------------
print("\nPermutations WITHOUT repetition:")
perm_no_repeat = permutations(digits_list, r)

for p in perm_no_repeat:
    print("".join(p))

# -----------------------------
# With Repetition
# -----------------------------
print("\nPermutations WITH repetition:")
perm_with_repeat = product(digits_list, repeat=r)

for p in perm_with_repeat:
    print("".join(p))