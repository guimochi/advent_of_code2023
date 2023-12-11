import time

start_time = time.time()

with open('input.txt', 'r') as f:
    pass

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")