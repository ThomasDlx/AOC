class Badge: # find common letter in 3 lines
    def __init__(self, badge: list[str]):
        self.badge = badge

    def define_badge(self):
        set_part_one = set(self.badge[0])
        set_part_two = set(self.badge[1])
        set_part_three = set(self.badge[2])

        common_letter = set_part_one.intersection(set_part_two).intersection(set_part_three)
        
        common_letter_str = ', '.join(common_letter)
        return common_letter_str 
        


class Bag: # reading a bag and returning common letters
    def __init__(self, bag: str):
        self.bag = bag

    def compart(self): # compare part of compartment 
        len_bag = len(self.bag)

        part_one = self.bag[:len_bag // 2]
        part_two = self.bag[len_bag // 2:]

        return set(part_one).intersection(set(part_two))


class DayThree: # reading bags and input file 
    def __init__(self, filename: str):
        self.sacs = self._init_input(filename)

    def __str__(self):
        return "\n".join(self.sacs)

    def _init_input(self, filename: str):
        bags = []
        with open(filename, "r") as file:
            for line in file:
                bags.append(line.strip())
        return bags

    def ord_letter(self,letter: str):
        self.letter = letter
        if ord('a') <= ord(letter) <= ord('z'):
            return ord(letter) - ord('a') + 1
        if ord('A') <= ord(letter) <= ord('Z'):
            return ord(letter) - ord('A') + 27

    def find_common_items_priority(self):
        total_priority = 0
        for sac in self.sacs:
            compartments = Bag(sac).compart()
            for item_type in compartments:
                total_priority += self.ord_letter(item_type)

        return total_priority
    
    def find_badge(self):
        total_badge = 0
        for i in range(0, len(self.sacs), 3):
            group_lines = self.sacs[i:i+3]
            common_letter = Badge(group_lines).define_badge()
            total_badge += self.ord_letter(common_letter)

        return total_badge

filename = "donnees_day3.txt"
sacs = DayThree(filename)
print("Common item :", sacs.find_common_items_priority())

print("Badge :", sacs.find_badge())




'''with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        len_line = len(line)
        first_part = line[:len_line // 2]
        second_part = line[len_line // 2:]
        print(line)
        print("taille de la chaine :", len_line)
        print("première partie de la chaine :", first_part)
        print("deuxième partie de la chaine :", second_part)
        
        ensemble1 = set(first_part)
        ensemble2 = set(second_part)
        
        common_letters = ensemble1.intersection(ensemble2)
        common_letters_str = ', '.join(common_letters)
        
        print("Lettres communes :", common_letters_str)
        
        for letter in common_letters:
            if letter in article_priorities:
                priority = article_priorities[letter]
                print(f"Priorité pour la lettre '{letter}': {priority}")
        
        print("---------------------")'''