def calculator():
    print("=================================")
    print("     SIMPLE PYTHON CALCULATOR    ")
    print("=================================")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == 2:
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == 3:
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == 4:
                if num2 == 0:
                    print("❌ Error! Division by zero is not allowed.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("⚠️ Invalid input! Please choose a number between 1 and 4.")
            
    except ValueError:
        print("⚠️ Invalid input! Please enter valid numeric values.")

if __name__ == "__main__":
    calculator()
