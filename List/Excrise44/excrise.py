#Generate Prime Numbers using List Comprehension
def get_primes(n):
    # A prime is any number not in the list of products (composites)
    composites = [j for i in range(2, 8) for j in range(i*2, n + 1, i)]
    primes = [x for x in range(2, n + 1) if x not in composites]
    return primes

# Test the function
limit = 20
result = get_primes(limit)

print(f"Primes up to {limit}: {result}")