import random


def generate_geometric_progression(length, start, ratio):
    return [start * (ratio ** i) for i in range(length)]

def play_geometric_progression_game(name):
    print("What number is missing in the progression?")
    for _ in range(3):
        length = random.randint(5, 10)
        start = random.randint(1, 10)
        ratio = random.randint(2, 5)
        progression = generate_geometric_progression(length, start, ratio)
        hidden_index = random.randint(0, length - 1)
        hidden_number = progression[hidden_index]
        progression[hidden_index] = ".."
        question = " ".join(map(str, progression))
        
        print(f"Question: {question}")
        user_answer = int(input("Your answer: "))
        
        if user_answer == hidden_number:
            print("Correct!")
            return
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{hidden_number}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")