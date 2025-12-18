import time
import sys

def print_header():
    print("="*40)
    print("      Welcome to My Python App      ")
    print("="*40)

def main():
    print_header()
    
    messages = [
        "Hello World from CMD!",
        "This program is running inside Docker.",
        "You can add any functionality you like!",
        "Enjoy coding 😎"
    ]
    
    for msg in messages:
        print(f"> {msg}")
        time.sleep(1)  # يعطي إحساس بالحركة تدريجياً
    
    print("\nAll tasks completed successfully!")
    print("\nAll tasks completed successfully!")
    print("\nSpecial thanks to my instructor: Nady Adel 🌟")
    print("="*40)

if __name__ == "__main__":
    main()
