import random
import time

def rowhammer(address):
    for i in range(100000):
        # Access the target row 100,000 times
        if address < len(memory): x = memory[address]

# Get the address of the target row
target_address = random.randint(0, 2**32)

# Initialize the memory
memory = [0] * 100000 # 2**32

# Start the attack
start = time.time()
rowhammer(target_address)
end = time.time()

# Print the time it took to trigger the attack
print("Time to trigger attack:", end - start)
