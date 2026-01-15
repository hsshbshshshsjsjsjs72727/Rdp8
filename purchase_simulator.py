import random

def generate_pin(length=6):
    """Generate a numeric PIN of specified length."""
    pin = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return pin

def main():
    print("Enter your choice:")
    print("1. Generate PIN")
    choice = input("Your choice: ").strip()
    if choice == '1':
        pin = generate_pin()
        print(f"Generated PIN: {pin}")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
