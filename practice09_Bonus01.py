# Vazifa: Foydalanuvchining balansi bor. U deposit, withdraw yoki check balance qiladi.

# Funksiyalar:

# deposit(balance, amount)
# withdraw(balance, amount)
# check_balance(balance)

def deposit(balance, amount):
    result = balance + amount
    return print(f"\nPulingiz qo'shildi! \n Balansda jami: {result} so'm")

def withdraw(balance, amount):
    result = balance - amount
    return print(f"\nPulingiz chiqarildi! \n Balansda qoldi: {result} so'm")

def check_balance(balance):
    return print(f"Balansingiz: {balance} so'm")

def main():
    balance = float(1_000_000)

    choice = int(input("\nBu Sizning elektron xamyoningiz"
                        "\n 1. Balansni tekshirish "
                        "\n 2. Pul chiqarish "
                        "\n 3. Pul to'ldirish "
                        "\n Nima qilamiz: "))

    if choice == 1:
        check_balance(balance)

    elif choice == 2:
        amount = float(input("\nChiqarmoqchi bo'lgan summangizni kiriting: "))

        if amount < balance and amount > 0:
            withdraw(balance, amount)

        else:
            print("Xato summa kiritingiz yoki balansingizda buncha summa mavjud emas")

    elif choice == 3:
        amount = float(input("\nTo'ldirmoqchi bo'lgan summangizni kiriting: "))

        if amount <= 10_000_000 and amount >= 5000:
            deposit(balance, amount)
        
        elif amount >= 10_000_000:
            print("Maksimal to'ldirish 10 million so'm")

        elif amount >= 0  and amount <= 4999:
            print("Minimal to'ldirish 5 ming so'm")
        
        else:
            print("Xato summa kiritingiz!")

    else:
        print("1, 2, 3 dan birini tanlang: ")


main()