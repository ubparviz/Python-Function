# Juft yoki Toq sonni aniqlash

def is_even(number: int) -> None:
    """Son qabul qiladi va uni toq yoki juft ekanligini tekshiradi

    Args:
        number (int): qandaydir butun son
    
    Returns: None
    """    
    if number % 2 == 0 and number != 0:
        print("Bu JUFT son")
    elif number == 0:
        print("0 juft ham emas toq ham emas")
    else:
        print("Bu TOQ son")


def main() -> None:
    """Son kiritishni so'raydi uni is_even funskisyasi orqali juft yoki toq ekanligini chiqartiradi
    va bu jarayonni cheksiz dav ettiradi

    Returns: None
    """    
    while True:
        number = int(input("Son kiriting: "))
        is_even(number)

main()