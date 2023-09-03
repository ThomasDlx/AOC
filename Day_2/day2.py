'''def calculate_score(adversaire, me):
    choices = {"A": 1, "B": 2, "C": 3,
               "X": 1, "Y": 2, "Z":3 }

    if adversaire in choices and me in choices:
        diff = choices[me] - choices[adversaire]

        if diff == 0:
            return choices[me] + 3
        elif diff == 1 or diff == -2:
            return choices[me] + 6
        else:
            return choices[me]
    else:
        return 0

total_score = 0

with open("donnees_day2.txt", "r") as file:
    for line in file:
        letter = line.strip().split()
        if len(letter) == 2:
            adversaire, me = letter
            total_score += calculate_score(adversaire, me)
print(total_score)'''

'''class Jeux:
    def __init__(self):
        self.choices = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    def calcul_score(self, adversaire, me):
        if adversaire in self.choices and me in self.choices:
            diff = self.choices[me] - self.choices[adversaire]

            if diff == 0:
                return self.choices[me] + 3
            elif diff == 1 or diff == -2:
                return self.choices[me] + 6
            else:
                return self.choices[me]
        else:
            return 0

    def calcul_total_score(self, filename):
        total_score = 0

        with open(filename, "r") as file:
            for line in file:
                letter = line.strip().split()
                if len(letter) == 2:
                    adversaire, me = letter
                    total_score += self.calcul_score(adversaire, me)

        return total_score

jeux = Jeux()
print(jeux.calcul_total_score("donnees_day2.txt"))'''

class Round:
    def __init__(self, me: str, elf: str):
        self.me = me
        self.elf = elf

    def __str__(self):
        return f"Round('{self.me}', '{self.elf}')"

    def calculate_score(self):
        choices = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

        if self.elf in choices and self.me in choices:
            diff = choices[self.me] - choices[self.elf]
            if diff == 0:
                return choices[self.me] + 3
            elif diff == 1 or diff == -2:
                return choices[self.me] + 6
            else:
                return choices[self.me]
        else:
            return 0
    
    def calculate_score_part_two(self):
        choices = {'A': 1, 'B': 2, 'C': 3, 'X' : 0, 'Y' : 3, 'Z': 6}
        swap_dict_loose = {"A": "C", "B": "A", "C": "B"}
        swap_dict_win = {"A": "B", "B": "C", "C": "A"}

        if self.elf in choices and self.me in choices:
            elf_choice = self.elf
            result = self.me

            if result == "X":   # défaite
                #print(f"elf_choice: {elf_choice}, my_choice {choices[swap_dict_loose[elf_choice]]} result: {choices[swap_dict_loose[elf_choice]]+choices[result]}")
                return choices[swap_dict_loose[elf_choice]] + choices[result]
            elif result == "Y": # égalité
                #print(f"elf_choice: {elf_choice},result : {choices[result]+choices[elf_choice]}")
                return choices[elf_choice] + choices[result]
            elif result == "Z": # victoire
                #print(f"elf_choice: {elf_choice}, my_choice {choices[swap_dict_win[elf_choice]]} result: {choices[swap_dict_win[elf_choice]]+choices[result]}")
                return choices[swap_dict_win[elf_choice]] + choices[result]

        else:
            return 0

class Game:
    def __init__(self, filename):
        self.rounds = self._init_round(filename)

    def __str__(self):
        return f"Game({', '.join(str(round) for round in self.rounds)})"

    def _init_round(self, filename):
        rounds = []
        with open(filename, "r") as file:
            for line in file:
                letter = line.strip().split()
                if len(letter) == 2:
                    adversaire, me = letter
                    round = Round(me, adversaire)
                    rounds.append(round)
        return rounds
   
    def calculate_total_score(self):
        total_score = 0
        for round in self.rounds:
            total_score += round.calculate_score()
        return total_score
    
    def calculate_total_score_part_two(self):
        total_score = 0
        for round in self.rounds:
            total_score += round.calculate_score_part_two()
        return total_score

game = Game("donnees_day2.txt")
print("Score de la game :",game.calculate_total_score())
print("Score de la part 2 :",game.calculate_total_score_part_two())
#print(game)