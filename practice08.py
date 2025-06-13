# Temperature Converter
# Vazifa: Celsius ↔ Fahrenheit aylantirish.

# °F=(°C×9/5)+32

def c_to_f(celsius):
    return (celsius * 9/5) + 32

# °C=(°F−32)×5/9

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    choice = input("Qaysi yo'nalishda aylantirmoqchisiz? \n 1. C→F "
                                                        "\n 2. F→C "
                                                        "\n Tanlang (1 yoki 2): ").lower()

    if choice == "1":
        c = float(input("Celsius ni kiriting: "))
        print("Natija:", c_to_f(c), "°F")
    elif choice == "2":
        f = float(input("Fahrenheit ni kiriting: "))
        print("Natija:", f_to_c(f), "°C")
    else:
        print("Sizda faqat 1 yoki 2 ni tanlash imkoni bor.")

main()
