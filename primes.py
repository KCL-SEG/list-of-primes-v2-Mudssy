"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <=0:
        raise ValueError
    
    counter = 0
    num = 2

    while counter != number_of_primes:
        is_prime = True
        i = 0
        length = len(list)
        while i < length and is_prime:
            if num % list[i] == 0:
                is_prime =  False
            i += 1
        
        if is_prime:
            list.append(num)
            counter += 1

        num += 1


    return list

