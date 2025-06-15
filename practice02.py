# Age Calculator

def calculate_age(birth_year: int, current_year: int) -> None:
    """
    Tug'ilgan yil va hozirgi yil asosida foydalanuvchining yoshini hisoblaydi.

    Parametrlar:
        birth_year (int): Tug'ilgan yil.
        current_year (int): Hozirgi yil.

    Natija:
        Ekranga foydalanuvchining yoshi va balog'atga yetgan-yetmaganligi haqidagi xabar chiqariladi.

    Returns: None
    """     
    age = current_year - birth_year
    print(f"Sizning yoshingiz: {age} yosh")

    if age >= 18:
        print("Siz balog'atga yetgansiz.")
    else:
        print("Siz balog'atga hali yetmagansiz.")

def main() -> None:
    """
    Foydalanuvchidan tug'ilgan yili va hozirgi yilni so'raydi,  
    so'ngra calculate_age() funksiyasi orqali yoshini hisoblaydi.

    Returns: None
    """
    birth_year = int(input("Nechinchi yil tug'ilgansiz: "))
    current_year = int(input("Hozir nechinchi yil: "))

    calculate_age(birth_year, current_year)


main()