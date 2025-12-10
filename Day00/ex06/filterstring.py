import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        assert all(c.isalpha() or c.isspace() for c in sys.argv[1]), \
            "the arguments are bad"
        assert sys.argv[2].isnumeric(), "the arguments are bad"

        print(ft_filter(lambda x: len(x) > int(sys.argv[2]),
                        sys.argv[1].split()))

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
