class SET:
    def __init__(self):
        self.elements = []

    # Input elements
    def input(self):
        n = int(input("Enter number of elements: "))
        print("Enter elements:")
        for _ in range(n):
            x = int(input())
            if not self.is_member(x):  # avoid duplicates
                self.elements.append(x)

    # Display set
    def display(self):
        print("{", " ".join(map(str, self.elements)), "}")

    # a. is_member
    def is_member(self, x):
        return x in self.elements

    # b. power set
    def power_set(self):
        n = len(self.elements)
        total = 1 << n  # 2^n

        print("Power Set:")
        for i in range(total):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(self.elements[j])
            print("{", " ".join(map(str, subset)), "}")

    # c. subset check
    def is_subset(self, other):
        for x in other.elements:
            if x not in self.elements:
                return False
        return True

    # d. union
    def union(self, other):
        result = SET()
        result.elements = self.elements.copy()
        for x in other.elements:
            if x not in result.elements:
                result.elements.append(x)
        return result

    # d. intersection
    def intersection(self, other):
        result = SET()
        for x in self.elements:
            if x in other.elements:
                result.elements.append(x)
        return result

    # e. complement
    def complement(self, universal):
        result = SET()
        for x in universal.elements:
            if x not in self.elements:
                result.elements.append(x)
        return result

    # f. difference (A - B)
    def difference(self, other):
        result = SET()
        for x in self.elements:
            if x not in other.elements:
                result.elements.append(x)
        return result

    # f. symmetric difference
    def symmetric_difference(self, other):
        result = SET()
        for x in self.elements:
            if x not in other.elements:
                result.elements.append(x)
        for x in other.elements:
            if x not in self.elements:
                result.elements.append(x)
        return result

    # g. cartesian product
    def cartesian_product(self, other):
        print("Cartesian Product:")
        for x in self.elements:
            for y in other.elements:
                print(f"({x}, {y})", end=" ")
            print()


# Main program
A = SET()
B = SET()
U = SET()

print("Enter Set A:")
A.input()

print("Enter Set B:")
B.input()

print("Enter Universal Set:")
U.input()

print("\nSet A =", end=" ")
A.display()

print("Set B =", end=" ")
B.display()

# is_member
x = int(input("\nEnter element to check in A: "))
print("True" if A.is_member(x) else "False")

# power set
A.power_set()

# subset
print("\nIs B subset of A?", "Yes" if A.is_subset(B) else "No")

# union
uni = A.union(B)
print("Union =", end=" ")
uni.display()

# intersection
inter = A.intersection(B)
print("Intersection =", end=" ")
inter.display()

# complement
comp = A.complement(U)
print("Complement of A =", end=" ")
comp.display()

# difference
diff = A.difference(B)
print("A - B =", end=" ")
diff.display()

# symmetric difference
sym = A.symmetric_difference(B)
print("Symmetric Difference =", end=" ")
sym.display()

# cartesian product
A.cartesian_product(B)