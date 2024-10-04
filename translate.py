import sys

# Dictionary for English to Braille
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OO.O', ':': '...OO.', ';': '...O..',
    'capital': '.....O', 'number': '.O.OOO'
}

# Reverse Braille dictionary for Braille to English translation
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Function to translate English to Braille
def english_to_braille(text):
    result = []
    for char in text:
        if char.isdigit():
            result.append(braille_dict['number'])  # Add number follows symbol
            result.append(braille_dict[char])
        elif char.isupper():
            result.append(braille_dict['capital'])  # Add capital follows symbol
            result.append(braille_dict[char.lower()])  # Translate character
        else:
            result.append(braille_dict.get(char, '?'))  # Translate character or unknown
    return ''.join(result)

# Function to translate Braille to English
def braille_to_english(braille_text):
    result = []
    is_capital = False
    is_number = False
    i = 0
    
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]  # Read the next 6 characters of Braille
        
        if braille_char == braille_dict['capital']:
            is_capital = True
        elif braille_char == braille_dict['number']:
            is_number = True
        elif braille_char == '......':  # Space
            result.append(' ')
            is_number = False  # Reset number mode after a space
        else:
            letter = reverse_braille_dict.get(braille_char, '?')
            if is_number:
                # Convert braille letters to digits
                if letter in 'abcdefghij':  
                    letter = str('1234567890'['abcdefghij'.index(letter)])
            if is_capital:
                letter = letter.upper()
                is_capital = False  # Only capitalize the next letter
            result.append(letter)
        i += 6
    
    return ''.join(result)

# Main function to detect input type and translate
if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:]).strip()

    # Check if input is Braille (i.e., consists of only dots and Os)
    if all(char in 'O.o' for char in input_text.replace(' ', '')):
        print("Braille Input:", input_text)
        print("English Translation:", braille_to_english(input_text))
    else:
        print("English Input:", input_text)
        print("Braille Translation:", english_to_braille(input_text))

