# Mini Quiz Game

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

def ask_question(question: str, correct_answer: str):
    user_answer = input(question + " ")
    if check_answer(user_answer, correct_answer):
        print("To'g'ri javob!")
    else:
        print("Noto'g'ri. To'g'ri javob:", correct_answer)

def main():
    print("Mini Quiz Game\n")

    # 1-savol
    ask_question("1. O'zbekiston poytaxti qaysi shahar?", "Toshkent")

    # 2-savol
    ask_question("2. 2 + 2 nechiga teng?", "4")

    # 3-savol
    ask_question("3. Dunyoda nechta davlat bor?", "227")

    # 4-savol
    ask_question("4. 2 * 2 + 2=?", "6")

    # 5-savol
    ask_question("O'zbekistondagi viloyatlar soni?", "12")

main()
