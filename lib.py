Morse = {'a': '.-', 'b': '-...', 'c': '-.-.',
           'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
           'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
           'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
           'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
           'z': '--..', '1': '.----', '2': '..---', '3': '...--',
           '4': '....-', '5': '.....', '6': '-....', '7': '--...',
           '8': '---..', '9': '----.', '0': '-----'}

Rotor = {'A': ['E', 'A', 'B', 'Y'], 'B': ['K', 'J', 'D', 'R'], 'C': ['M', 'D', 'F', 'U'],
         'D': ['F', 'K', 'H', 'H'], 'E': ['L', 'S', 'J', 'Q'], 'F': ['G', 'I', 'L', 'S'],
         'G': ['D', 'R', 'C', 'L'], 'H': ['Q', 'U', 'P', 'D'], 'I': ['V', 'X', 'R', 'P'],
         'J': ['Z', 'B', 'T', 'X'], 'K': ['N', 'L', 'X', 'N'], 'L': ['T', 'H', 'V', 'G'],
         'M': ['O', 'W', 'Z', 'O'], 'N': ['W', 'T', 'N', 'K'], 'O': ['Y', 'M', 'Y', 'M'],
         'P': ['H', 'C', 'E', 'I'], 'Q': ['X', 'Q', 'I', 'E'], 'R': ['U', 'G', 'W', 'B'],
         'S': ['S', 'Z', 'G', 'F'], 'T': ['P', 'N', 'A', 'Z'], 'U': ['A', 'P', 'K', 'C'],
         'V': ['I', 'Y', 'M', 'W'], 'W': ['B', 'F', 'U', 'V'], 'X': ['R', 'V', 'S', 'J'],
         'Y': ['C', 'O', 'Q', 'A'], 'Z': ['J', 'E', 'O', 'T']}
Ru = 'йцукенгшщзхъфывапролджэячсмитьбю'
reply_keyboard = [['Шифр Цезаря', 'Двоичный код'],
                  ['Enigma', 'Morse'], ['return']]
cip_keyboard = [['Зашифровать', 'Расшифровать'], ['return']]
return_keyboard = [['return']]
start_keyboard = [['/mastermind']]