# Vazifa: Og‘irlik va bo‘y kiritiladi → BMI va uning holati chiqadi.

# Funksiya:

# calculate_bmi(weight: float, height: float) -> float
# bmi_status(bmi: float) -> str

def calculate_bmi(weight: float, height: float) -> float:
    """Foydalanuvchini bo'yi va vaznidan foydalanib BMI raqamini chiqarib beradi

    Args:
        weight (float): foydalanuvchining vazni (kg)
        height (float): bo'yi (metr)

    Returns:
        float: bmi natijasi
    """    
    return round(weight / (height ** 2), 2)

def bmi_status(bmi: float) -> str:
    """Foydalanuvchini BMI raqamidan foydalanib uni holatini chiqarib beradi

    Args:
        bmi (float): foydalanuvchini BMI raqami

    Returns:
        str: Holati
    """    
    if bmi < 18.5:
        return "Ozg'in"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Semiz"
    
def main() -> None:
    """
    Foydalanuvchidan bo'yi va vaznini so'raydi
    O'shanga qarab BMI raqami va holatini chiqarib beradi
    Funksiyalardan foydalanadi
    """    
    weight = float(input("Vazningizni kiriting (kg): "))
    height = float(input("Bo'yingizni kiriting (metrlarda): "))
    
    bmi = calculate_bmi(weight, height)
    status = bmi_status(bmi)

    print(f"\nBMI: {bmi}")
    print(f"Holati: {status}")

main()