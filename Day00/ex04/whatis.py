import sys

if __name__ == "__main__":
    
    try:
        if len(sys.argv) == 1:
            exit(0)

        assert len(sys.argv) == 2, "more than one argument is provided"
        
        num = int(sys.argv[1])
        
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

            # throw error
    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError: argument is not an integer")
