# Foydalanuvchi ball kiritadi → A, B, C, F baho qaytadi.

def get_grade(score: int) -> bool:
    """Foydalanuvchi kiritgan 0-100 gacha ball orqali uni natijasini chiqarib beradi

    Args:
        score (int): Ball

    Returns:
        bool: Keyinchalik While siklini to'xtatish uchun True yoki False qaytaradi
    """      
    if score <= 100 and score >= 91:
        print("A")
        return True
    elif score <= 90 and score >= 81:
        print("B")
        return True
    elif score <= 80 and score >= 71:
        print("C")
        return True
    elif score <= 70 and score >= 60:
        print("F")
        return True
    elif score <= 59 and score >= 0:
        print("Imtihondan yiqildingiz!")
        return True
    else:
        print("Ball 0-100 gacha oraliqda bo'lishi kerak!")
        return False

def main() -> None:
    """
    Foydalanuvchidan butun son so'raydi uni get_grade funksiyadi orqli hisoblaydi

    Agar foydalanuvchi 0-100 oraliqda ball kiritmasa xato qilganini aytib qayta qayta ball kiritishni so'rayveradi.
    To'g'ri son kiritilganda to'xtaydi

    Returns: None
    """
    while True:
        score = int(input("Ballingizni kiriting: "))
        if get_grade(score):
            break

main()
