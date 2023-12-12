# The cache serves to avoid redundant calculations of the same result. If we branch off, we might end up calculating
# the same subsequent state multiple times. To prevent this, each time we traverse through the function, we check if
# we have previously encountered the current situation. We only compute the result if it's our first encounter;
# otherwise, we retrieve the value from the cache.
cache = {}


# This function checks the first letter of cfg and creates the next possible configurations if possible If it can
# determine whether the cfg is valid or not, it returns 1 or 0 accordingly cfg tracks the current configuration,
# we always look at the first element nums tracks the expected number of blocks, we always look at the first element
# flag tracks if the last element we checked was a block
# Note: we never pass a nums where the first element is 0. So if the flag is false, the first nums is never 0. We
# ensure that we remove any leading 0s.
def count(cfg: str, nums: [int], flag=False):
    def inner():
        # no more string left to check
        if cfg == "":
            return 1 if sum(nums) == 0 else 0
        # no more block left to check
        if sum(nums) == 0:
            return 0 if "#" in cfg else 1
        # check block
        if cfg[0] == "#":
            # checking a block and one more broken comes in
            if flag and nums[0] == 0:
                return 0
            # reduce the nb for this block, important to create a new block because it might be referenced somewhere
            # else, set flag to true
            return count(cfg[1:], (nums[0] - 1, *nums[1:]), True)
        # check spring
        if cfg[0] == ".":
            # if i am expecting more blocks
            if flag and nums[0] > 0:
                return 0
            # here, both options work
            # recurse with next nums if we just finished a block, with the current nums otherwise
            # return count(cfg[1:], nums if not flag else nums[1:])
            # we recurse with the current nums if there is still value in there, with the next num otherwise
            return count(cfg[1:], nums[1:] if nums[0] == 0 else nums)
        # the only option left is for cfg is ?
        # check if we are looking through a block
        if flag:
            # if the block should end, we consider the ? a spring
            if nums[0] == 0:
                return count(cfg[1:], nums[1:])
            # the block should continue, we consider the ? a block
            return count(cfg[1:], (nums[0] - 1, *nums[1:]), True)
        # this a ? and we are not currently, scanning a block
        # we can consider whatever we like because the first 2 checks we did assured that we are not in an ending state
        # we first consider it a spring so not much happens and we consider it a block so we have to adapt accordingly
        return count(cfg[1:], nums) + count(cfg[1:], (nums[0] - 1, *nums[1:]), True)

    # For this key to work, we need to replace the list of nums as tuple.
    key = (cfg, nums, flag)

    # we will only calculate this if it is necessary
    if key not in cache:
        cache[key] = inner()

    return cache[key]


with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))

        cfg = "?".join([cfg] * 5)
        nums *= 5

        total += count(cfg, nums)
    print(total)
