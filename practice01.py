# Calculator (Kalkulyator)

def add(a: float, b: float) -> str:
    """
    Ikkita sonni qo'shadi va natijani matn ko'rinishida qaytaradi.

    Parameters:
        a (float): Birinchi son.
        b (float): Ikkinchi son.
    Returns:
        str: amal natijasi (matn ko'rinishida).
    """
    result = a + b
    return f"{a} + {b} = {result}"

def subtract(a: float, b: float) -> str:
    """
    Ikkita sonni ayiradi va natijani matn ko'rinishida qaytaradi.

    Parameters:
        a (float): Birinchi son.
        b (float): Ikkinchi son.
    Returns:
        str: amal natijasi (matn ko'rinishida).
    """
    result = a - b
    return f"{a} - {b} = {result}"

def multiply(a: float, b: float) -> str:
    """
    Ikkita sonni ko'paytiradi va natijani matn ko'rinishida qaytaradi.

    Parameters:
        a (float): Birinchi son.
        b (float): Ikkinchi son.
    Returns:
        str: amal natijasi (matn ko'rinishida).
    """
    result = a * b
    return f"{a} * {b} = {result}"

def divide(a: float, b: float) -> str:
    """
    Ikkita sonni bo'ladi va natijani matn ko'rinishida qaytaradi.

    Parameters:
        a (float): Birinchi son.
        b (float): Ikkinchi son.
    Returns:
        str: amal natijasi (matn ko'rinishida).
    """
    result = a / b
    return f"{a} / {b} = {result}"

def main() -> None:
    """
    Kalkulyator dasturining asosiy menyusi.

    Foydalanuvchidan ikki son va matematik amal turini so'raydi.
    Amalga qarab tegishli funksiyani chaqiradi va natijani ekranga chiqaradi.

    Qo'llab-quvvatlanadigan amallar:
        + — qo'shish
        - — ayirish
        * — ko'paytirish
        / — bo'lish (0 ga bo'linishga ruxsat yo'q)

    Returns: None
    """
    a: float = float(input("Birinchi sonni kiriting: "))
    op: str = input("Amalni kiriting (+, -, *, /): ")
    b: float = float(input("Ikkinchi sonni kiriting: "))

    if op == "+":
        print(add(a, b))

    elif op == '-':
        print(subtract(a, b))

    elif op == '*':
       print(multiply(a, b))

    elif op == '/':
        if b == 0:
            print("Son 0 ga bo'linmaydi")
        else:
            print(divide(a, b))

    else:
        print("wrong operator")


main()