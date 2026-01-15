import random
import time
import sys

STABLE_US_AREA_CODES = ['213', '310', '415', '408', '646', '917', '312', '773']
SERVICES = {
    '1': 'Google / Gmail',
    '2': 'TikTok',
    '3': 'Telegram',
    '4': 'WhatsApp'
}

def generate_phone_number(area_code):
    prefix = random.randint(200, 999)
    line_number = random.randint(1000, 9999)
    return f"+1-{area_code}-{prefix}-{line_number}"

def select_service():
    print("Select the exact service name:")
    for key, service in SERVICES.items():
        print(f"{key}. {service}")
    choice = input("Enter your choice (1-4): ").strip()
    while choice not in SERVICES:
        print("Invalid choice. Please select a valid service number.")
        choice = input("Enter your choice (1-4): ").strip()
    return SERVICES[choice]

def select_area_code():
    print("\nChoose Stable US Area Codes (commonly reliable):")
    print(", ".join(STABLE_US_AREA_CODES))
    area_code = input("Enter area code from above list: ").strip()
    while area_code not in STABLE_US_AREA_CODES:
        print("Invalid area code. Please select from the list.")
        area_code = input("Enter area code from above list: ").strip()
    return area_code

def simulate_sms_code():
    return ''.join(str(random.randint(0, 9)) for _ in range(6))

def main():
    print("=== Phone Number Purchase Simulator ===")
    country = "United States (+1)"
    print(f"Country: {country}")

    service = select_service()
    area_code = select_area_code()
    phone_number = generate_phone_number(area_code)

    print("\nPurchase Summary:")
    print(f"Country: {country}")
    print(f"Service: {service}")
    print(f"Status: Pending")
    print(f"Time left: 15 minutes")
    print(f"Phone Number: {phone_number}")

    print("\nYou have 15 minutes to enter the code from SMS.")
    print("Enter your choice:")
    print("1. Continue")
    print("2. Cancel")

    start_time = time.time()
    time_limit = 15 * 60  # 15 minutes in seconds

    while True:
        if time.time() - start_time > time_limit:
            print("Time expired. Status: Failed.")
            sys.exit(1)

        choice = input("Enter your choice (1 to continue, 2 to cancel): ").strip()
        if choice == '1':
            sms_code = simulate_sms_code()
            print(f"SMS code received: {sms_code}")
            print("Status: Successful")
            print(f"RESULT: PhoneNumber={phone_number} SMSCode={sms_code} Service={service}")
            break
        elif choice == '2':
            print("Purchase cancelled.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
