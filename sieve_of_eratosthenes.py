def sieve_of_eratosthenes(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1
    return [i for i, is_prime in enumerate(primes) if is_prime]


def find_prime_with_most_consecutive_primes(limit):
    primes = sieve_of_eratosthenes(limit)
    max_consecutive = 0
    prime_with_most_consecutive = 0

    for i in range(len(primes)):
        sum_of_primes = primes[i]
        consecutive = 1

        for j in range(i + 1, len(primes)):
            sum_of_primes += primes[j]
            consecutive += 1

            if sum_of_primes > limit:
                break

            if sum_of_primes in primes and consecutive > max_consecutive:
                max_consecutive = consecutive
                prime_with_most_consecutive = sum_of_primes

    return prime_with_most_consecutive


limit = 1000000
result = find_prime_with_most_consecutive_primes(limit)
print("The prime number below one million that can be written as the sum of the most consecutive primes is:", result)
