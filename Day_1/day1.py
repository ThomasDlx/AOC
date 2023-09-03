'''current_elf_calories:int = 0
max_calories:int = 0



with open("donnees_day1.txt","r") as file:
    for line in file:
        if line.strip():
            current_elf_calories += int(line)
        else:
            max_calories = max(max_calories, current_elf_calories)
            current_elf_calories = 0

print(max_calories)'''

'''class Elf:
    def __init__(self):
        self.calories = []

    def add_calories(self, calories:int):
        self.calories.append(calories)

    def sum(self):
        return sum(self.calories)

max_calories = 0

with open("donnees_day1.txt", "r") as file:
    current_elf = Elf()
    for line in file:
        if line.strip():
            current_elf.add_calories(int(line))
        else:
            calorie_current = current_elf.sum()
            max_calories = max(calorie_current, max_calories)
            current_elf = Elf()
    
print(max_calories)'''

'''from typing import List

class Elf:
    def __init__(self, calories: List[int]):
        self.calories = calories

    def sum(self):
        return sum(self.calories)

class ElfManager:
    def __init__(self):
        self.elves = []

    def add_elf(self, elf: Elf):
        self.elves.append(elf)

    def calculate_max_calories(self):
        max_calories = 0
        for elf in self.elves:
            calorie_current = elf.sum()
            max_calories = max(calorie_current, max_calories)
        return max_calories

    def calculate_top_three_calories(self):
        sorted_elves = sorted(self.elves, key=lambda elf: elf.sum(), reverse=True)
        top_three_elves = sorted_elves[:3]
        total_calories = sum(elf.sum() for elf in top_three_elves)
        return total_calories

    def read_elves_from_file(self, filename: str):
        with open(filename, "r") as file:
            current_elf_calories = []
            for line in file:
                line = line.strip()
                if line:
                    current_elf_calories.append(int(line))
                else:
                    if current_elf_calories:
                        elf = Elf(current_elf_calories)
                        self.add_elf(elf)
                    current_elf_calories = []

            if current_elf_calories:
                elf = Elf(current_elf_calories)
                self.add_elf(elf)

filename = "donnees_day1.txt"
elf_manager = ElfManager()
elf_manager.read_elves_from_file(filename)

max_calories = elf_manager.calculate_top_three_calories()
print("Top Three Calories:", max_calories)
'''


class Elf:
    def __init__(self):
        self.calories:list[int] = []
    
    def add_calories(self,calories):
        self.calories.append(calories)

    def sum_calories(self):
        return sum(self.calories)

class ElfManager:
    def __init__(self, filename:str):
        self.elves:list[Elf] = self._init_elf_manager(filename)

    def _init_elf_manager(self, filename):
        elves = []
        with open(filename, "r") as file:
            current_elf = Elf()
            for line in file:
                line = line.strip()
                if line:
                    current_elf.add_calories(int(line))
                else:
                    if current_elf.calories:
                        elves.append(current_elf)
                        current_elf = Elf()
        return elves
    
    def max_calories(self):
        return max(elf.sum_calories() for elf in self.elves)
    
    def max_top_three(self):
        sorted_elves = sorted(self.elves, key=lambda elf: elf.sum_calories(), reverse=True)
        somme = 0
        for i in range(3):  
            somme += sorted_elves[i].sum_calories()
        return somme

elves = ElfManager("donnees_day1.txt")
print(elves.max_calories())
print("top :",elves.max_top_three())
