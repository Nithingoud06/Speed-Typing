import time
import random

def generate_random_text():
    words = ["python", "programming", "challenge", "coding", "speed", "typing", "test", "development", "algorithm", "debugging"]
    return ' '.join(random.choices(words, k=10))

def speed_typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter when you are ready to start...")
    
    start_time = time.time()
    
    # Generate random text for typing
    text_to_type = generate_random_text()
    print("\nType the following text:")
    print(text_to_type)
    
    user_input = input("\nYour typing: ")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Calculate words per minute (WPM)
    words_typed = len(user_input.split())
    wpm = (words_typed / elapsed_time) * 60
    
    # Compare user input with the generated text
    if user_input == text_to_type:
        print(f"\nCongratulations! You typed it correctly.")
        print(f"Your typing speed: {wpm:.2f} words per minute.")
    else:
        print("\nSorry, there are mistakes in your typing. Try again.")

if __name__ == "__main__":
    speed_typing_test()
