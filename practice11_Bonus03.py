# tax Calculator
# Vazifa: Maoshni kiritadi → soliqni hisoblab beradi.
# Soliq stavkasi o‘zgarishi mumkin (masalan, >5mln bo‘lsa 20%, boshqacha 13%).

def calculate_soliq(maosh):
    if maosh > 5_000_000:
        return maosh * 0.20
    else:
        return maosh * 0.13

def calculate_sof_maosh(maosh):
    soliq = calculate_soliq(maosh)
    return maosh - soliq

def main():
    maosh = float(input("Oylik maoshingizni kiriting (so'mda): "))
    
    soliq = calculate_soliq(maosh)
    sof_maosh = calculate_sof_maosh(maosh)

    print(f"\n Soliq: {soliq} so'm")
    print(f"\n Sof maosh: {sof_maosh} so'm")

main()
