from googletrans import Translator

# Dictionary mapping language codes to language names
languages = {
    '1': 'telugu',
    '2': 'kannada',
    '3': 'tamil',
    '4': 'malayalam',
    '5': 'chinese (simplified)',
    '6': 'french',
    '7': 'hindi',
    '8': 'spanish',
    '9': 'korean',
    '10': 'japanese'
}

def convert(text, x):
    translator = Translator()
    translated = translator.translate(text, dest=x)
    return translated.text

def print_language_menu():
    print("Welcome to the Language Translator!")
    print("Select a language to translate to:")
    for key, value in languages.items():
        print(f"{key}. {value.capitalize()}")

def condition():
    while True:
        print_language_menu()
        selection = input("Enter the number corresponding to the language you want to translate to (or 'exit' to quit): ").strip()

        if selection.lower() == 'exit':
            return None
        elif selection in languages:
            return languages[selection]
        else:
            print("Invalid selection. Please enter a valid number or 'exit'.")

def main():
    while True:
        x = condition()

        if not x:
            print("Exiting the Language Translator.")
            break

        given = input("Enter the text you want to translate (or 'exit' to quit): ").strip()

        if given.lower() == 'exit':
            print("Exiting the Language Translator.")
            break

        y = convert(given, x)

        print(f"\n\nTranslated text ({x.capitalize()}): {y}\n")

if __name__ == "__main__":
    main()
