# Mini Quiz Game

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def ask_question(question, correct_answer):

    user_answer = input(question + " ")

    if check_answer(user_answer, correct_answer):
        print("To'g'ri javob!")
    else:
        print("Noto'g'ri. To'g'ri javob:", correct_answer)

def main():
    print("Mini Quiz Game\n")

    # 1-savol
    ask_question("1. Dunyoda nechta davlat bor?", "227")

    # 2-savol
    ask_question("2. 2 * 2 + 2=?", "6")

    # 3-savol
    ask_question("3. O'zbekistondagi viloyatlar soni?", "12")

main()
