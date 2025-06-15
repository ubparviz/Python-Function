# Mini Quiz Game

def check_answer(user_answer: str, correct_answer: str) -> bool:
    """
    Foydalanuvchi javobini to'g'ri javob bilan solishtiradi (katta-kichik harflarni e'tiborga olmaydi).

    Parametrlar:
        user_answer (str): Foydalanuvchining kiritgan javobi.
        correct_answer (str): To'g'ri javob.

    Returns:
        bool: Javob to'g'ri bo'lsa True, aks holda False qaytaradi.
    """
    return user_answer.lower() == correct_answer.lower()

def ask_question(question: str, correct_answer: str) -> None:
    """
    Savol so'raydi va foydalanuvchi javobini tekshiradi.

    Parametrlar:
        question (str): Savol.
        correct_answer (str): To'g'ri javob.

    Returns: None
    """
    user_answer = input(question + " ")

    if check_answer(user_answer, correct_answer):
        print("To'g'ri javob!")
    else:
        print("Noto'g'ri. To'g'ri javob:", correct_answer)

def main():
    """Mini quiz o'yini uchun asosiy funksiya.""" 

    print("Mini Quiz Game\n")

    # 1-savol
    ask_question("1. Dunyoda nechta davlat bor?", "227")

    # 2-savol
    ask_question("2. 2 * 2 + 2=?", "6")

    # 3-savol
    ask_question("3. O'zbekistondagi viloyatlar soni?", "12")

main()
