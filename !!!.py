from joblib import Parallel, delayed

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_consecutive_primes(start, end):
    max_consecutive = 0
    current_consecutive = 0
    for num in range(start, end + 1):
        if is_prime(num):
            current_consecutive += 1
            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive
        else:
            current_consecutive = 0
    return max_consecutive

def main():
    num_processes = 4  # Кількість процесів для паралельного обчислення
    limit = 1000000

    chunk_size = limit // num_processes
    start_values = [i * chunk_size + 1 for i in range(num_processes)]
    end_values = [(i + 1) * chunk_size for i in range(num_processes)]

    results = Parallel(n_jobs=num_processes)(
        delayed(find_consecutive_primes)(start, end)
        for start, end in zip(start_values, end_values)
    )

    max_consecutive = max(results)
    print("Найбільша послідовність простих чисел:", max_consecutive)

if __name__ == '__main__':
    main()
