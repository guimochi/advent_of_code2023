import time

start_time = time.time()

# get last from list
def last(liste):
    return len(liste) - 1


with open('input.txt', 'r') as f:
    total = 0
    for line in f.readlines():
        # get inputs
        nums = [(list(map(int, line.split())))]
        j = 0
        # create the serie of nb
        while (sum(nums[len(nums) - 1]) != 0):
            new_serie = []
            for i in range(1, len(nums[j])):
                new_serie.append(nums[j][i] - nums[j][i - 1])
            nums.append(new_serie)
            j += 1

        # add lat numbers
        nums[last(nums)].insert(0, 0)
        for i in range(last(nums), 0, -1):
            i_first = 0
            current_num = nums[i][i_first]
            last_num = nums[i - 1][i_first]
            nums[i - 1].insert(i_first, last_num - current_num)
        print(nums)
        total += nums[0][0]
    print(total)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
