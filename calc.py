def calculator():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"1. Add. \n2. Subtract. \n3. Multiply. \n4. Divide. \n5. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                add = num1 + num2
                print("Here is the result: ", add)
            elif choice == "2":
                sub = num1 - num2
                print("Here is the result: ", sub)
            elif choice == "3":
                mul = num1 * num2
                print("Here is the result: ", mul)
            elif choice == "4":
                if num2 == 0:
                    print("can't do that brodie")
                else:
                    div = num1 / num2
                    print("Here is the result: ", div)
            elif choice == "5":
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("That aint a number, brodie")


calculator()
