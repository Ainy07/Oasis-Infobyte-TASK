import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("No character types selected")

    return ''.join(random.choice(character_set) for _ in range(length))

def main():
    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
