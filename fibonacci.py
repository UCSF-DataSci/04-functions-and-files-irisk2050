#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import os
import argparse

def fibonacci_generator_to_limit(num_limit):
    # Do something
    print(num_limit)
    fibonacci_nums = []
    if num_limit >= 2:
          fibonacci_nums = [0, 1, 1]
          small_fib = fibonacci_nums[-2]
          big_fib = fibonacci_nums[-1]
          while (small_fib + big_fib) < num_limit:
                next_fib = small_fib + big_fib
                fibonacci_nums.append(next_fib)
                small_fib = big_fib
                big_fib = next_fib

    elif num_limit == 1:
          fibonacci_nums.append(0)
    return fibonacci_nums

if __name__ == "__main__":
    # Do stuff here
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers until a given limit and save to file fibonacci_100.txt.")
    parser.add_argument("num_limit", type=int, help="Upper limit for Fibonacci numbers.")
    parser.add_argument("output_file", type=str, help="Output file to save Fibonacci sequence.")

    args = parser.parse_args()
    num_limit = args.num_limit
    output_file = args.output_file
    
    if os.path.exists(output_file):
        print(f"The file '{output_file}' already exists and will be overwritten.")
    else:
        print(f"The file '{output_file}' does not exist. It will be created.")

    # Generate Fibonacci numbers
    fibonacci_sequence = fibonacci_generator_to_limit(num_limit)

    # Handle file writing
    try:
        with open(output_file, 'w') as f:
            for num in fibonacci_sequence:
                f.write(f"{num}\n")
        print(f"Successfully wrote Fibonacci sequence to {output_file}")
    except OSError:
        print("An OSError occurred!")