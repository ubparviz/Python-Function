#  Number Guessing Game (Random ishlatilmaydi)
# Vazifa: Kompyuterda sirli son mavjud. Foydalanuvchi taxmin qiladi. To‘g‘ri yoki xato deyilgan bo‘ladi.

def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("To'g'ri topdingiz!")
    else:
        print("Xato")

def main():
    
    secret_number = 69
    while True:

        guess = int(input("Sirli sonni toping (1 dan 100 gacha): "))

        is_correct = check_guess(secret_number, guess)
        print_result(is_correct)

        if is_correct:
            break

main()

