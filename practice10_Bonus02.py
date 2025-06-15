# Parol kiritiladi. Uzunligi 8 dan uzun bo'lsa kuchli aks holda kuchsiz. 

def is_strong_password(password: str) -> None:
    """Foydalanuvchidan parol qabul qiladi uni kuchli yoki kuchsiz ekanligini tekshiradi

    Args:
        password (str): Kiritilgan parol

    Returns: NONE
    """    
    if len(password) >= 8:
        print("Parol kuchli")
    
    elif len(password) < 8 and len(password) >= 4:
        print("Parol kuchsiz")
    
    elif len(password) < 4:
        print("Eng kamida 4 ta belgi bo'lsin")

def main() -> None:
    """Parol so'raydi va is_strong_password funksiyasini ishga tushiradi

    Returns: NONE
    """    
    password = input("Parol kiriting: ")

    is_strong_password(password)

main()