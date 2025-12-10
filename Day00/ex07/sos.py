import sys


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        assert all((c.isalnum() or c.isspace()) for c in sys.argv[1]), \
            "the arguments are bad"

        NESTED_MORSE = {" ": "/ ", 'A': '.-', 'B': '-...',
                        'C': '-.-.', 'D': '-..', 'E': '.',
                        'F': '..-.', 'G': '--.', 'H': '....',
                        'I': '..', 'J': '.---', 'K': '-.-',
                        'L': '.-..', 'M': '--', 'N': '-.',
                        'O': '---', 'P': '.--.', 'Q': '--.-',
                        'R': '.-.', 'S': '...', 'T': '-',
                        'U': '..-', 'V': '...-', 'W': '.--',
                        'X': '-..-', 'Y': '-.--', 'Z': '--..',
                        '1': '.----', '2': '..---', '3': '...--',
                        '4': '....-', '5': '.....', '6': '-....',
                        '7': '--...', '8': '---..', '9': '----.',
                        '0': '-----'}

        str_code = sys.argv[1].upper()

        str_formated = ""

        for c in str_code:
            if c in NESTED_MORSE:
                str_formated += NESTED_MORSE[c]

        print(str_formated)

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
