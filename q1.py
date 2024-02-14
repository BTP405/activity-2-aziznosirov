def getPrimeNumbers(n): 
    prime_numbers = [num for num in range(2, n+1) if is_prime(num)]
    print(prime_numbers)
    
def is_prime(num):
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False

    return True
    

