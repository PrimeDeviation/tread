import sys

def connect_tab():
    print("Scanning for Bluetooth devices...")
    # Simulated delay
    import time
    time.sleep(1)
    print("Found device: Treadmill (Address: 4F:98:56:B5:52:5B)")

def sessions_tab():
    print("Sessions Tab: Display list of past sessions.")

def current_session_tab():
    print("Current Session Tab: Create a new session, start/stop treadmill, adjust speed.")

def main():
    print("Treadmill App Prototype")
    print("1. Connect")
    print("2. Sessions")
    print("3. Current Session")
    choice = input("Enter choice: ")
    if choice == '1':
        connect_tab()
    elif choice == '2':
        sessions_tab()
    elif choice == '3':
        current_session_tab()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
