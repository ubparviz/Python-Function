# Telefon raqam 9 ta raqamdan iboratligini tekshiradi.

def is_valid_phone_number(phone):

    if phone.isdigit() and len(phone) == 9:
        return print("Raqam to'g'ri kiritildi")
    
    else:
        return  print("Telefon raqam 9 ta raqamdan iborat bo'lishi kerak")

def main():
    phone = input("Telefon raqamingizni kiriting (991234567): ")

    is_valid_phone_number(phone)

main()
