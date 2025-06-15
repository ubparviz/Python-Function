# Palindrome Checker (faqat str bilan)
# Vazifa: So‘z kiritiladi → teskari o‘qiganda ham bir xilmi, yo‘qmi tekshiriladi.

# Funksiya:

# is_palindrome(text: str)

def is_palindrome(text: str) -> bool:
    """Foydalanuvchi kiritgan so'zni PALLINDROM ekanligini tekshiradi

    Args:
        text (str): Foydalanuvchi kiritadigan so'z

    Returns:
        bool: agar PALLINDROM bo'lsa TRUE, aks holda FALSE qaytaradi
    """    
    return text.lower() == text[::-1].lower()

def main() -> None:
    """
    Foydalanuvchidan so'z kiritishini so'raydi va funksiyalarni ishga tushuradi
    Foydalanuvchi raqam qatnashgan so'z kiritsa toki to'g'ri so'z kiritmaguncha qayta-qayta so'rayveradi

    Returns: NONE
    """    
    while True:
        text = input("\nSo'z kiriting: ")

        if text.isalpha():
            if is_palindrome(text):
                print("\nBu so'z PALINDROM")
            else:
                print("\nYo'q PALINDROM emas")
        else:
            print("\nFaqat so'z kiriting va so'zda raqam qatnashmasin")

main()