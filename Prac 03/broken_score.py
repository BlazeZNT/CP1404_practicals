"""80
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(change_score_to_result(score))


def change_score_to_result(score):
    if score > 100 or score < 0:
        return "The score is invalid"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()
