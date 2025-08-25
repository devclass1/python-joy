# Basic try-except block
def basic_error_handling():
    print("=== Basic Error Handling ===")
    
    # This will cause a ZeroDivisionError
    try:
        result = 10 / 0
    except:
        print("An error occurred!")
    
    # Handling specific exceptions
    try:
        num = int("not_a_number")
    except ValueError as e:
        print(f"ValueError: {e}")
    
    # Handling multiple exceptions
    try:
        # This could cause either a ValueError or ZeroDivisionError
        num = int(input("Enter a number: "))
        result = 100 / num
        print(f"Result: {result}")
    except ValueError:
        print("That's not a valid number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the basic error handling example
basic_error_handling()
