def fibonacci_generator_to_limit(num_limit):
    # Do something
    if num_limit == 0:
        return []
    elif num_limit == 1:
        return [0]
    fibonacci_nums = [0, 1]
    while (fibonacci_nums[-1] + fibonacci_nums[-2]) < num_limit:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    
    return fibonacci_nums

def is_prime(num):
    if num <= 1:
        return False
    elif num > 1:
        for i in range(2, ((num // 2) + 1)):
            if num % i == 0:
                return False
    return True