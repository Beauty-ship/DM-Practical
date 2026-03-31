class RELATION:
    def __init__(self):
        self.n = 0
        self.matrix = []

    # Input relation as matrix
    def input(self):
        self.n = int(input("Enter number of elements in set: "))
        print("Enter the relation matrix (0 or 1):")
        
        self.matrix = []
        for i in range(self.n):
            row = list(map(int, input().split()))
            self.matrix.append(row)

    # Display matrix
    def display(self):
        print("Relation Matrix:")
        for row in self.matrix:
            print(row)

    # Reflexive: all diagonal elements = 1
    def is_reflexive(self):
        for i in range(self.n):
            if self.matrix[i][i] != 1:
                return False
        return True

    # Symmetric: if (i,j)=1 then (j,i)=1
    def is_symmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    # Anti-symmetric: if (i,j)=1 and (j,i)=1 then i == j
    def is_antisymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

    # Transitive: if (i,j)=1 and (j,k)=1 then (i,k)=1
    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == 1:
                    for k in range(self.n):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            return False
        return True

    # Check relation type
    def check_relation(self):
        reflexive = self.is_reflexive()
        symmetric = self.is_symmetric()
        antisymmetric = self.is_antisymmetric()
        transitive = self.is_transitive()

        print("\nProperties:")
        print("Reflexive:", reflexive)
        print("Symmetric:", symmetric)
        print("Anti-symmetric:", antisymmetric)
        print("Transitive:", transitive)

        if reflexive and symmetric and transitive:
            print("\nRelation is an Equivalence Relation")
        elif reflexive and antisymmetric and transitive:
            print("\nRelation is a Partial Order Relation")
        else:
            print("\nRelation is None")


# Main program
R = RELATION()

R.input()
R.display()
R.check_relation()
