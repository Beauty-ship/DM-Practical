def evaluate_polynomial(coeff, n):
    result = 0
    power = len(coeff) - 1

    for c in coeff:
        result += c * (n ** power)
        power -= 1

    return result


# Example polynomial: 4n^2 + 2n + 9
coeff = [4, 2, 9]

n = int(input("Enter value of n: "))

result = evaluate_polynomial(coeff, n)

print("Value of polynomial =", result)