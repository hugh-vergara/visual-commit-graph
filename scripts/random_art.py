import random

patterns = [
    "*-*-*-*-*-*-*-*-*-*-*-*",
    "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~",
    "= = = = = = = = = = = =",
    "# # # # # # # # # # # #",
    "@ @ @ @ @ @ @ @ @ @ @ @"
]

if __name__ == '__main__':
    choice = random.choice(patterns)
    print('Here is some random art:')
    for _ in range(5):
        print(choice)
