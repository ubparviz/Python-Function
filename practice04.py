# Foydalanuvchi ball kiritadi → A, B, C, F baho qaytadi.

def get_grade(score):
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

def main():
    while True:
        score = int(input("Ballingizni kiriting: "))
        if get_grade(score):
            break

main()
