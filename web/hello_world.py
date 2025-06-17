def get_user_name():
    """Get the user's name through input."""
    return input("Please enter your name: ")

def create_greeting(name):
    """Create a personalized greeting message."""
    return f"Hello, {name}! Welcome to the AI Native Journey! 🚀"

def main():
    # Get the user's name
    user_name = get_user_name()
    
    # Create and display the greeting
    greeting = create_greeting(user_name)
    print("\n" + greeting)
    print("\nWe're excited to have you join us on this AI development journey!")

if __name__ == "__main__":
    main() 