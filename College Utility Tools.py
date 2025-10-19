from utils import reg_generator, reg_finder, odd_even_finder, password_generator

def menu():
    print("""
College Utility Tools
1. Generate registration numbers
2. Find registration numbers in text
3. Find odd/even numbers
4. Generate password
5. Exit
""")

while True:
    menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        year = input("Enter year: ")
        branch = input("Enter branch code: ")
        start = int(input("Start roll no: "))
        end = int(input("End roll no: "))
        for reg in reg_generator.generate_reg_numbers(year, branch, start, end):
            print(reg)

    elif choice == "2":
        text = input("Enter text: ")
        found = reg_finder.find_reg_numbers(text)
        print("Found registration numbers:", found if found else "None")

    elif choice == "3":
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("Odd numbers:", odd_even_finder.find_odd(nums))
        print("Even numbers:", odd_even_finder.find_even(nums))

    elif choice == "4":
        length = int(input("Enter password length: "))
        print("Generated password:", password_generator.generate_password(length))

    elif choice == "5":
        break

    else:
        print("Invalid choice, try again.")
