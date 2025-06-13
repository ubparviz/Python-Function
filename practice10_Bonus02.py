# Parol kiritiladi. Uzunligi 8 dan uzun bo'lsa kuchli aks holda kuchsiz. 

def is_strong_password(password):
    if len(password) >= 8:
        print("Parol kuchli")
    
    elif len(password) < 8 and len(password) >= 4:
        print("Parol kuchsiz")
    
    elif len(password) < 4:
        print("Eng kamida 4 ta belgi bo'lsin")

def main():
    password = input("Parol kiriting: ")

    is_strong_password(password)

main()