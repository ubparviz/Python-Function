# tax Calculator
# Vazifa: Maoshni kiritadi → soliqni hisoblab beradi.
# Soliq stavkasi o‘zgarishi mumkin (masalan, >5mln bo‘lsa 20%, boshqacha 13%).

def calculate_soliq(maosh: float) -> float:
    """Maosh qarab soliqni qancha chiqishini hisoblab beradi

    Args:
        maosh (float): foydalanuvchini maoshi
    Returns:
        float: soliq
    """    
    if maosh > 5_000_000:
        soliq = maosh * 0.20
        return soliq
    else:
        soliq = maosh * 0.13
        return soliq

def calculate_sof_maosh(maosh: float, soliq: float) -> float:
    """Moashdan soliqni olib tashlaydi. Sof maoshni hisoblaydi.
    Args:
        maosh (float): oladigan maosh
        soliq (float): soliq

    Returns:
        float: sof maosh
    """
    sof_maosh = maosh - soliq   
    return sof_maosh

def main()-> None:
    """
    Foydalanuvchidan qancha maosh olishini so'raydi.
    Shunga qarab soliq va sof daromadini chiqarib beradi
    """    
    maosh = float(input("Oylik maoshingizni kiriting (so'mda): "))

    soliq = calculate_soliq(maosh)
    sof_maosh = calculate_sof_maosh(maosh, soliq)

    print(f"\n Soliq: {soliq:.2f} so'm")
    print(f"\n Sof maosh: {sof_maosh:.2f} so'm")

main()
