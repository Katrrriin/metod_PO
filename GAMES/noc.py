import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def play_game(name):
    print("Find the smallest common multiple of given numbers.")
    for _ in range(3):
        numbers = [random.randint(1, 100) for _ in range(3)]
        question = " ".join(map(str, numbers))
        corr_ans = lcm(lcm(numbers[0], numbers[1]), numbers[2])
        print(f"Question: {question}")
        user_answer = int(input("Your answer: "))
        if user_answer == corr_ans:
            print("Correct!")
            return
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{corr_ans}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")