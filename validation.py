def validationInput():
    # Get user input
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("Please enter a number")
        return validationInput()