import random

def generate_pin():
    pin = random.randint(1000, 9999)
    return pin

if __name__ == "__main__":
    print("Generated PIN:", generate_pin())
