import random

word_list = ["code", "harshita", "hello"]
random_item = random.choice(word_list)
print(random_item)

user_input = input("Guess A Letter: ").lower()
size = len(random_item)
string_to_repeat = "_"
blanks_list = [string_to_repeat] * size
isfound = False
guesses =0
def find(user_input):
    global isfound
    founded_pos = -1
    for i in range(size):
        if random_item[i] == user_input:
            founded_pos = i
            blanks_list[i] = user_input
            isfound = True
    return founded_pos

def checkfound():
    global isfound, guesses
    if isfound:
        print("Found!", user_input)
        print("".join(blanks_list))
    else:
        print("Not found.")
        guesses += 1

while "".join(blanks_list) != random_item:
    isfound = False
    founded_pos = find(user_input)
    checkfound()
    user_input = input("Guess A Letter: ").lower()

print("Congratulations! You guessed the word:", random_item)
print("Total Guesses:", guesses)
