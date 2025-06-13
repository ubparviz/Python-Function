# Palindrome Checker (faqat str bilan)
# Vazifa: So‘z kiritiladi → teskari o‘qiganda ham bir xilmi, yo‘qmi tekshiriladi.

# Funksiya:

# is_palindrome(text: str)

def is_palindrome(text):
    return text.lower() == text[::-1].lower()

def main():
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