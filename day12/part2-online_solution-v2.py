import time

start_time = time.time()

cache = {}


def count(cfg, nums):
    # check si on est dans le cache, la fonction ne sera lance que si on n'est pas dedans
    # key = (cfg, nums)
    # if key in cache:
    #     return cache[key]

    if cfg == "":
        return 1 if not nums else 0
    if not nums:
        return 0 if "#" in cfg else 1

    results = 0
    # dans le cas ou c'est . ou ? on va continuer a parcourir ou le consider comme un .
    if cfg[0] in ".?":
        results += count(cfg[1:], nums)
    # dans le cas ou c'est un # ou ?. on va faire le check pour voir s'il est possible ce continuer
    if cfg[0] in "#?":
        if (
            # il y a assez de places pour que ce soit possible
            nums[0] <= len(cfg)
            # s'il y a un point par les nums[0] prochain caractere
            and "." not in cfg[: nums[0]]
            # si le caractere apres le block est vide ou n'est pas un #
            and (len(cfg) == nums[0] or cfg[nums[0]] != "#")
        ):
            # on continue le scenario en passant au caractere suivant
            results += count(cfg[nums[0] + 1 :], nums[1:])

    # enregistre le resultat dans le cache
    # cache[key] = results
    return results


with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))

        cfg = "?".join([cfg] * 5)
        nums *= 5

        total += count(cfg, nums)
    print(total)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
