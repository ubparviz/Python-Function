# Vazifa: Foydalanuvchining balansi bor. U deposit, withdraw yoki check balance qiladi.

# Funksiyalar:

# deposit(balance, amount)
# withdraw(balance, amount)
# check_balance(balance)

balance = 100

def deposit(balance: float, amount: float) -> float:
    """
    Balansga mablag' qo'shadi.

    Parametrlar:
        balance (float): Joriy balans.
        amount (float): Qo'shiladigan summa.

    Returns:
        float: Yangi balans qiymati.
    """
    if amount <= 10_000 and amount >= 5:
        balance += amount
        print(f"\nPulingiz qo'shildi! \n Balansda jami: {balance}$")
        return balance
    
    elif amount >= 10_000:
        print("\n=== Maksimal to'ldirish 10 ming $ ===")
        return balance
    
    elif amount >= 0  and amount < 5:
        print("\n=== Minimal to'ldirish 5$ ===")
        return balance
    
    else:
        print("Xato summa kiritingiz!")
        return balance

def withdraw(balance: float, amount: float) -> float:
    """
    Balansdan mablag' ayiradi.

    Parametrlar:
        balance (float): Joriy balans.
        amount (float): Ayriladigan summa.

    Returns:
        float: Yangi balans qiymati.
    """
    if amount < balance and amount > 0:
        balance -= amount
        print(f"\nPulingiz chiqarildi! \n Balansda qoldi: {balance}$")
        return balance
    
    else:
        print("Xato summa kiritingiz yoki balansingizda buncha summa mavjud emas")
        return balance

def check_balance() -> None:
    """
    Balansni ekranga chiqaradi.
    Returns: None
    """
    print(f"Balansingiz: {balance}$")

def main():
    """
    Foydalanuvchiga asosiy menyuni chiqaradi.
    Foydalanuvchi tanlagan tanlov orqali funksiyalarni ishga tushiradi
    """
    while True:
        
        choice = int(input("\nBu Sizning elektron xamyoningiz"
                            "\n 1. Balansni tekshirish "
                            "\n 2. Pul chiqarish "
                            "\n 3. Pul to'ldirish "
                            "\n Nima qilamiz: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            amount = float(input("\nChiqarmoqchi bo'lgan summangizni kiriting: "))
            withdraw(balance, amount)

        elif choice == 3:
            amount = float(input("\nTo'ldirmoqchi bo'lgan summangizni kiriting: "))
            deposit(balance, amount)

        else:
            print("\n=== 1, 2, 3 dan birini tanlang ===")


main()