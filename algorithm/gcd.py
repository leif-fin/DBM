def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Calculate the greatest common divisors of 15 and 25
print("GCD of 15 and 25:", gcd(15, 25))
