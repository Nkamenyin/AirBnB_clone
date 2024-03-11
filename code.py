def greet(name):
    """Print a greeting message."""
    print(f"Hello, {name}!")

# Main program
if __name__ == "__main__":
    # Get user input for their name
    user_name = input("Enter your name: ")

    # Call the greet function with the user's name
    greet(user_name)
