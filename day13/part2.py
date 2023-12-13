import time

start_time = time.time()


# transpose all blocks seperatly
def transpose_blocks(blocks: [[str]]):
    return [transpose_block(block) for block in blocks]


# transpose a block
def transpose_block(block):
    lists_chrs = [list(s) for s in block]
    transposed = zip(*lists_chrs)
    transposed_strings = ["".join(t) for t in transposed]
    return transposed_strings


# sum all reflexives rows together
def sum_ref_row(blocks):
    nb_rows = nb_cols = 0
    for block in blocks:
        # get the reflexive row or col with the smudge
        r, c = get_r_or_c_with_smudge(block)
        nb_rows += r
        nb_cols += c
    return nb_rows, nb_cols


# get the reflexive row and ignores a smudge
def get_smudge(block):
    candidates_rr, r_to_line = get_candidates_rr_and_map(block)
    # iterate candidate the find the one
    for crr in candidates_rr:
        up = crr
        down = crr - 1
        differences = 0
        # while in the block
        while down >= 0 and up < len(block):
            # retain nb of differences
            differences += sum_smudge(block[up], block[down])
            up += 1
            down -= 1
            if differences > 1:
                break
        if differences == 1:
            return crr
    return 0


# check 2 lines and return the sum of differences btw them
def sum_smudge(line1, line2):
    return sum(1 for a, b in zip(line1, line2) if a != b)


# return the value of the row or col with the smudge
def get_r_or_c_with_smudge(block):
    r_smudge = get_smudge(block)
    # we return if we found it, otherwise we check the columns
    if r_smudge:
        return r_smudge, 0
    c_smudge = get_smudge(transpose_block(block))
    return 0, c_smudge


# get the candidates the center of reflexion by checking if the row and the row before are identique
def get_candidates_rr_and_map(block):
    r_line: {int: str} = {}
    # row of possible reflection
    possible_center: [int] = []
    # add everything
    for r, line in enumerate(block[1:], 1):
        r_line[r] = block[r]
        r_line[r - 1] = block[r - 1]
        # the last condition would have been really hard to find without the exemple
        # I have to check if 2 adjacents row could transform in the center of reflecion. I don't think I would have
        # thought of it without the exemple
        if block[r] == block[r - 1] or sum_smudge(block[r], block[r - 1]) == 1:
            possible_center.append(r)
    return possible_center, r_line


with open("input.txt", "r") as f:
    blocks = f.read().split("\n\n")
    blocks = [block.split("\n") for block in blocks]
    rows, cols = sum_ref_row(blocks)
    print(cols + 100 * rows)


end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
