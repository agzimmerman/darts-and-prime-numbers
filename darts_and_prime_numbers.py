''' This script answers a question that came up while playing darts at Sowieso the other night.
Someone observed that, when you look at any two adjacent sections, their number very often summed to prime numbers.
We counted nine.
I suppose I should double check that number on a standard dart board found on the internet, and put that here.
But for now the question is: Is this actually unusual? If someone were to place the numbers at random, then, on average, how many adjacent pairs would sum to prime numbers?



*** SPOILER ALERT!!! ***


Unless there is a mistake in this script (which is quite likely), the expected value is six, but the variance is four,
so the observed count on a standard dart board is within two standard deviations, and therefore not so remarkable.



Tested on Python 2.7.12 :: Anaconda custom (64-bit)
'''

import random
import math
import numpy

''' This is a function for checking if a number is prime, found at https://stackoverflow.com/questions/18833759/python-prime-number-checker'''
def is_prime(n):

    if n % 2 == 0 and n > 2: 
    
        return False
        
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
    


''' A dart board is divided into twenty sections, each with a unique number from 1 to 20 
Achtung! This can lead to confusion in this script, because we index the sections from 0 to 19.'''
section_count = 20

numbers = range(1, section_count + 1)


''' We employ the Monte Carlo integration method to estimate the expected value of the number of ajacted pairs that sum to a prime number.
'''
large_number = 10000

report_at = (100, 1000, 10000)

prime_counts = []


''' Run the Monte Carlo loop '''
for sample in range(1, large_number + 1):

    random.shuffle(numbers) # This randomizes the order of the list of numbers, modifying the list in place
    
    
    ''' Count the adjacted pairs that sum to prime numbers '''
    prime_count = 0
    
    for section in range(section_count):
    
        adjacent_section = (section + 1)%(section_count - 1) # Handle the periodic boundary condition
        
        if is_prime(numbers[section] + numbers[adjacent_section]):
        
            prime_count += 1
            
    prime_counts.append(prime_count)
    

    ''' Update the expected value, and report it regularly to check for convergence '''
    if sample in report_at:
    
        print('With a sample size of '+str(sample)+', the expected value is '+str(numpy.mean(prime_counts))+' and the variance is '+str(numpy.var(prime_counts)))
        