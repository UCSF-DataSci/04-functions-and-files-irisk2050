#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

import os
import argparse
import mymodule

def largest_prime_fibonacci(num_limit):
    fib_nums = mymodule.fibonacci_generator_to_limit(num_limit)
    prime_fibs = [num for num in reversed(fib_nums) if mymodule.is_prime(num)]
    if prime_fibs:
        print(max(prime_fibs))
        return max(prime_fibs)
    else:
        print("No prime Fibonacci numbers.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the largest prime Fibonacci number until a given limit.")
    parser.add_argument("--num_limit", "-n", type=int, help="Upper limit for Fibonacci numbers.")
    parser.add_argument("--output_file", "-o", type=str, help="Output file to save largest prime Fibonacci number.")

    args = parser.parse_args()
    num_limit = args.num_limit
    output_file = args.output_file
    os.chdir("/Users/iriskim/Desktop/04-functions-and-files-irisk2050/")
    
    if os.path.exists(output_file):
         print(f"The file '{output_file}' already exists and will be overwritten.")
    else:
        print(f"The file '{output_file}' does not exist. It will be created.")
        
    max_prime_fib = largest_prime_fibonacci(num_limit)
        
    # Handle file writing
    try:
        with open(output_file, 'a') as f:
            f.write(f"Limit: {num_limit}, max prime Fibonacci number: {max_prime_fib}\n")
        print(f"Successfully wrote largest prime Fibonacci number to {output_file}.")
    except OSError:
        print("An OSError occurred!")