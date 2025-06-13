# Age Calculator

def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    print(f"Sizning yoshingiz: {age} yosh")

    if age >= 18:
        print("Siz balog'atga yetgansiz.")
    else:
        print("Siz balog'atga hali yetmagansiz.")

def main():
    birth_year = int(input("Nechinchi yil tug'ilgansiz: "))
    current_year = int(input("Hozir nechinchi yil: "))

    calculate_age(birth_year, current_year)


main()