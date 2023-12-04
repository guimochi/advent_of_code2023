with (open("part1", "r") as f):
    sum = 0
    for line in f.readlines():
        card, num_values = line.split(":")
        winning_part, actual_part = num_values.split('|')
        win_nbs = set(winning_part.split())
        actual_nbs = set(actual_part.split())

        print(win_nbs, actual_nbs)

        first_add = True
        calcul = 0
        for win_nb in win_nbs:
            if win_nb in actual_nbs:
                if first_add:
                    first_add = False
                    calcul = 1
                    continue
                calcul *= 2

        sum += calcul
    print(sum)