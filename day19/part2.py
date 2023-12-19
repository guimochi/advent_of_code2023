import re
import time

start_time = time.time()


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


with open("test.txt", "r") as f:
    workflows_str = f.read().split("\n\n")[0]
    workflows_str = [line.strip("}").split("{") for line in workflows_str.split("\n")]
    workflows = {}
    for workflow in workflows_str:
        workflows[workflow[0]] = Workflow(workflow[0], workflow[1])


end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
