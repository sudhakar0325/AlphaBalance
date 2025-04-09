while True:
    string = input("Enter a string: ").strip()
    if not string:
        print("Please enter a non-empty string")
        continue
        
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonant_count = 0

    for char in string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    if vowel_count == consonant_count:
        print(f"Equal counts: {vowel_count} vowels and {consonant_count} consonants")
    elif vowel_count > consonant_count:
        print(f"Vowels ({vowel_count}) exceed consonants ({consonant_count})")
    else:
        print(f"Consonants ({consonant_count}) exceed vowels ({vowel_count})")

    if input("Continue? (yes/no): ").lower() not in ['yes', 'y']:
        print("Goodbye!")
        break
