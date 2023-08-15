#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    
    # Iterate through each argument
    for arg in sys.argv[1:]:
        # Convert argument to integer and add to total
        total += int(arg)
    
    # Print the total
    print(total)
