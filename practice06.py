# Telefon raqam 9 ta raqamdan iboratligini tekshiradi.

def is_valid_phone_number(phone: str):
    """
    Telefon raqam to'g'ri kiritilganini tekshiradi.

    Args:
        phone (str): Foydalanuvchi tomonidan kiritilgan telefon raqam (faqat raqamlardan iborat bo'lishi kerak).

    Result:
        Raqam 9 xonali bo'lsa — to'g'ri deb chiqaradi,
        Aks holda — xatolik xabari beradi.

    Returns: None
    """

    if phone.isdigit() and len(phone) == 9:
        print("Raqam to'g'ri kiritildi")
    
    else:
        print("Telefon raqam 9 ta raqamdan iborat bo'lishi kerak")

def main():
    """Foydalanuvchidan string so'raydi va uni is_valid_phone_number orqali tekshiradi"""
    
    phone = input("Telefon raqamingizni kiriting (991234567): ")

    is_valid_phone_number(phone)

main()
