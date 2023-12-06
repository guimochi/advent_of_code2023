with open('input.txt', 'r') as f:
    all_lines = f.readlines()
    line = [int(all_lines[0].split(':')[1].strip(' \n').replace(' ', ''))]
    t = [int(all_lines[0].split(':')[1].strip(' \n').replace(' ', ''))]
    dist = [int(all_lines[1].split(':')[1].strip(' \n').replace(' ', ''))]
    record = 1
    for i in range(len(t)):
        reached = 0
        for j in range(1, t[i]):
            travel = j * (t[i] - j)
            if travel > dist[i]:
                reached += 1
        record *= reached

    print(record)
