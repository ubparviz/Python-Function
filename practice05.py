#  Number Guessing Game (Random ishlatilmaydi)
# Vazifa: Kompyuterda sirli son mavjud. Foydalanuvchi taxmin qiladi. To‘g‘ri yoki xato deyilgan bo‘ladi.

# Global O'zgaruvchi
secret_number = 69

def check_guess(guess: int) -> bool:
    """Sirli son bilan foydalanuvchi kiritgan son tengmi tekshiradi

    Args:
        guess (int): butun son qabul qiladi

    Returns:
        bool: Tekshiradi, TRUE yoki FALSE chiqaradi
    """    
    return secret_number == guess

def print_result(is_correct: bool) -> None:
    """Foydalanuvchi topdimi yoki yo'q aniqlashtiradi

    Args:
        is_correct (bool): True yoki False qabul qiladi
    
    Returns: None
    """    
    if is_correct:
        print("To'g'ri topdingiz!")
    else:
        print("Xato")

def main() -> None:
    """Barcha funskiyalarni ishga tushiradi foydalanuvchi to'g'ri sonni topmaganchu bu funksiya to'xtamaydi"""    
    while True:
        guess = int(input("Sirli sonni toping (1 dan 100 gacha): "))

        is_correct = check_guess(guess)
        print_result(is_correct)

        if is_correct:
            break

main()

