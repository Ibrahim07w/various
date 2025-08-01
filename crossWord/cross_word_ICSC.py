import random

def CreateCrosswords(words, size):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    modes = ['horizontal', 'vertical', 'diagonal','upward']
    crossWord = [[random.choice(alphabet) for _ in range(size)] for _ in range(size)]
    occupied = set()
    def can_place(word, i, j, dx, dy):
        for k in range(len(word)):
            ni, nj = i + k*dx, j + k*dy
            if not (0 <= ni < size and 0 <= nj < size):
                return False
            if (ni, nj) in occupied and crossWord[ni][nj] != word[k]:
                return False
        return True
    def place(word, i, j, dx, dy):
        for k in range(len(word)):
            ni, nj = i + k*dx, j + k*dy
            crossWord[ni][nj] = word[k]
            occupied.add((ni, nj))
    for word in words:
        word = word.upper()
        placed = False
        while not placed:  
            direction = random.choice(modes)
            if direction == 'horizontal':
                i = random.randint(0, size - 1)
                j = random.randint(0, size - len(word))
                if can_place(word, i, j, 0, 1):
                    place(word, i, j, 0, 1)
                    placed = True
            elif direction == 'vertical':
                i = random.randint(0, size - len(word))
                j = random.randint(0, size - 1)
                if can_place(word, i, j, 1, 0):
                    place(word, i, j, 1, 0)
                    placed = True
            elif direction == 'diagonal':
                i = random.randint(0, size - len(word))
                j = random.randint(0, size - len(word))
                if can_place(word, i, j, 1, 1):
                    place(word, i, j, 1, 1)
                    placed = True
            elif direction == 'upward':
                i = random.randint(len(word) - 1, size - 1)
                j = random.randint(0, size - 1)
                if can_place(word, i, j, -1, 0):
                    place(word, i, j, -1, 0)
                    placed = True
        if not placed:
            print(f"Failed to place word: {word}")
    for row in crossWord:       # print the crossword
        print(' '.join(row))

for _ in range(5):
    CreateCrosswords(['ibrahim', 'khalid'], 10)
    print("\n" + "="*30 + "\n")
