import sys


def main():
    """This Program which takesa single string argument and
    displays the sums of its upper-case characters, lower-case
    characters, punctuation characters, digits, and spaces."""
    try:
        if len(sys.argv) == 1 or len(sys.argv) == 2 and sys.argv[1] == "":
            print("What is the text to count?")
            user_input = sys.stdin.read()
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            user_input = sys.argv[1]

        up = 0
        low = 0
        punc = 0
        spaces = 0
        digits = 0

        for char in user_input:
            if char in r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                punc += 1
            elif char.isupper():
                up += 1
            elif char.islower():
                low += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1

        print("The text contains", len(user_input), "characters:")
        print(up, "upper letters")
        print(low, "lower letters")
        print(punc, "punctuation marks")
        print(spaces, "spaces")
        print(digits, "digits")

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("unexpected error:", e)


if __name__ == "__main__":
    main()
