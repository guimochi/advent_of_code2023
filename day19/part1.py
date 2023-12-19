import re
import time

start_time = time.time()


class Part:
    def __init__(self, args):
        for key, value in args.items():
            setattr(self, key, int(value))
        self.visited = set()

    def get_rating(self, category: str):
        return getattr(self, category, None)

    def get_value(self):
        return self.x + self.m + self.a + self.s

    def add_visit(self, workflow):
        self.visited.add(workflow)


class Workflow:
    def __init__(self, name, conditions):
        self.name = name
        self.conditions = [
            re.split("([<>])|:", condition) for condition in conditions.split(",")
        ]

    def get_next_stop(self, part):
        for condition in self.conditions[:-1]:
            if condition[1] == "<" and part.get_rating(condition[0]) < int(
                condition[2]
            ):
                return condition[4]
            elif condition[1] == ">" and part.get_rating(condition[0]) > int(
                condition[2]
            ):
                return condition[4]
        return self.conditions[len(self.conditions) - 1][0]


with open("input.txt", "r") as f:
    workflows_str, parts_str = f.read().split("\n\n")
    parts_str = [line.strip("{}") for line in parts_str.split("\n")]
    workflows_str = [line.strip("}").split("{") for line in workflows_str.split("\n")]
    workflows = {}
    for workflow in workflows_str:
        workflows[workflow[0]] = Workflow(workflow[0], workflow[1])

    parts = []
    for part in parts_str:
        dict = {}
        pieces = part.split(",")
        for piece in pieces:
            cut = piece.split("=")
            dict[cut[0]] = cut[1]
        parts.append(Part(dict))

    accepted = set()
    rejected = set()

    for part in parts:
        next_stop = "in"
        while True:
            next_stop = workflows[next_stop].get_next_stop(part)
            if next_stop == "A":
                accepted.add(part)
                break
            elif next_stop == "R":
                rejected.add(part)
                break
            elif next_stop in part.visited:
                rejected.add(part)
                break
    print(sum([a.get_value() for a in accepted]))


end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
