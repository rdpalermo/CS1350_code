# CS1350AAMidterm
# October 15, 2026
# Ronald Palermo
###############################################################
# PROBLEM 1: COURSE GRADEBOOK
class Gradebook:
    def __init__(self):
        self.grades = {}

    def add_score(self, student, assignment, score):
        if student not in self.grades:
            self.grades[student] = {}

        self.grades[student][assignment] = score

    def student_average(self, student):
        if student not in self.grades or not self.grades[student]:
            return None

        scores = self.grades[student].values()
        return sum(scores) / len(scores)

    def assignment_average(self, assignment):
        scores = []

        for student in self.grades:
            if assignment in self.grades[student]:
                scores.append(self.grades[student][assignment])

        if not scores:
            return None

        return sum(scores) / len(scores)

    def top_students(self, n):
        averages = []

        for student in self.grades:
            average = self.student_average(student)

            if average is not None:
                averages.append((student, average))

        averages.sort(key=lambda item: item[1], reverse=True)

        return [student for student, average in averages[:n]]

    def missing(self, assignment):
        missing_students = []

        for student in self.grades:
            if assignment not in self.grades[student]:
                missing_students.append(student)

        return sorted(missing_students)


# Test cases
gb = Gradebook()
gb.add_score("Alice", "hw1", 90)
gb.add_score("Alice", "hw2", 80)
gb.add_score("Bob", "hw1", 70)
gb.add_score("Bob", "hw2", 60)
gb.add_score("Carol", "hw1", 100)
gb.add_score("Bob", "hw2", 75)

print(gb.student_average("Alice"))
print(gb.student_average("Bob"))
print(gb.student_average("Zed"))
print(gb.assignment_average("hw1"))
print(gb.assignment_average("hw9"))
print(gb.top_students(2))
print(gb.missing("hw2"))

#################################################################
# PROBLEM 2: ACCESS CONTROL WITH SETS
class Door:
    def __init__(self, name):
        self.name = name
        self.authorized_cards = set()

    def grant(self, card_id):
        self.authorized_cards.add(card_id)

    def revoke(self, card_id):
        self.authorized_cards.discard(card_id)

    def can_open(self, card_id):
        return card_id in self.authorized_cards


def master_cards(doors):
    if not doors:
        return set()

    result = doors[0].authorized_cards.copy()

    for door in doors[1:]:
        result = result & door.authorized_cards

    return result


def single_door_cards(doors):
    counts = {}

    for door in doors:
        for card in door.authorized_cards:
            counts[card] = counts.get(card, 0) + 1

    return {card for card in counts if counts[card] == 1}


def unused_cards(all_cards, doors):
    used = set()

    for door in doors:
        used = used | door.authorized_cards

    return all_cards - used


def audit(doors):
    for door in doors:
        print(f"{door.name}: {len(door.authorized_cards)} cards")

    print("Master cards:", master_cards(doors))


# Test cases
lobby = Door("Lobby")
for c in [101, 102, 103, 104]:
    lobby.grant(c)

lab = Door("Lab")
for c in [101, 103, 105]:
    lab.grant(c)

server = Door("Server Room")
for c in [101, 105]:
    server.grant(c)

lab.revoke(105)
lab.revoke(999)

print(lab.can_open(103), lab.can_open(105))

doors = [lobby, lab, server]

print(master_cards(doors))
print(single_door_cards(doors))
print(unused_cards({101, 102, 105, 200}, doors))

audit(doors)
#########################################################