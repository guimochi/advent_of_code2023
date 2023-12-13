import time

start_time = time.time()


def transpose_blocks(blocks: [[str]]):
    ret = []
    for block in blocks:
        lists_chrs = [list(s) for s in block]
        transposed = zip(*lists_chrs)
        transposed_strings = ["".join(t) for t in transposed]
        ret.append(transposed_strings)
    return ret


def check_prev(centers: [int], r_line: {int: str}):
    for center in centers:
        valid = True

    pass


def ref_row(blocks):
    nb_row = 0
    for block in blocks:
        # retain which line is where
        r_line: {int: str} = {}
        # row of possible reflection
        possible_center: [int] = []
        # add everything
        for r, line in enumerate(block[1:], 1):
            r_line[r] = block[r]
            r_line[r - 1] = block[r - 1]
            if block[r] == block[r - 1]:
                possible_center.append(r)

        # iter to look for reflexion
        for center in possible_center:
            up = center
            down = center - 1
            valid = True
            while down >= 0 and up < len(block):
                if r_line[up] != r_line[down]:
                    valid = False
                    break
                up += 1
                down -= 1
            if valid:
                nb_row += center

    return nb_row
    pass


with open("input.txt", "r") as f:
    blocks = f.read().split("\n\n")
    blocks = [block.split("\n") for block in blocks]
    rows = ref_row(blocks)
    print("rows", rows)
    tr_blocks = transpose_blocks(blocks)
    cols = ref_row(tr_blocks)
    print("cols", cols)
    print(cols + 100 * rows)
    pass

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
