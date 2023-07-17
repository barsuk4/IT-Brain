from joblib import Parallel, delayed

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_with_most_consecutive_primes(limit):
    primes = [n for n in range(2, limit) if is_prime(n)]
    max_consecutive = 0
    prime_with_most_consecutive = 0

    def check_consecutive_sum(start_index):
        nonlocal max_consecutive
        nonlocal prime_with_most_consecutive

        sum_of_primes = 0
        consecutive = 0
        for i in range(start_index, len(primes)):
            sum_of_primes += primes[i]
            consecutive += 1
            if sum_of_primes > limit:
                break
            if is_prime(sum_of_primes) and consecutive > max_consecutive:
                max_consecutive = consecutive
                prime_with_most_consecutive = sum_of_primes

    Parallel(n_jobs=-1)(delayed(check_consecutive_sum)(i) for i in range(len(primes)))

    return prime_with_most_consecutive

limit = 1000000
result = find_prime_with_most_consecutive_primes(limit)
print("Просте число менше одного мільйона, яке може бути записане як сума найбільшої послідовності простих чисел:", result)
