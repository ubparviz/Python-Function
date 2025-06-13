# Vazifa: Og‘irlik va bo‘y kiritiladi → BMI va uning holati chiqadi.

# Funksiya:

# calculate_bmi(weight: float, height: float) -> float
# bmi_status(bmi: float) -> str

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def bmi_status(bmi):
    if bmi < 18.5:
        return "Ozg'in"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Semiz"
    
def main():
    weight = float(input("Vazningizni kiriting (kg): "))
    height = float(input("Bo'yingizni kiriting (metrlarda): "))
    
    bmi = calculate_bmi(weight, height)
    status = bmi_status(bmi)

    print(f"\nBMI: {bmi}")
    print(f"Holati: {status}")

main()