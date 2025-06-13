# Juft yoki Toq sonni aniqlash

def is_even(number):
    if number % 2 == 0 and number != 0:
        print("Bu JUFT son")
    elif number == 0:
        print("0 juft ham emas toq ham emas")
    else:
        print("Bu TOQ son")

def main():
    while True:
        number = int(input("Son kiriting: "))
        is_even(number)

main()