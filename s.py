import sys

def main():
    print(f"sys.argv prints all the arguments at the cmd including file name ")
    print(f"len(sys.argv) prints the toatal number of arg in cmd{len(sys.argv)}")


    for arg in sys.argv:
        print(arg)

if __name__ == "__main__":
    main()


# # HELP FINCTION in terminal
# import math
# dir(math)

# dir(srt)
# dir(int)
# dir(random)

# import calculator
# dir(calculator)
# dir(float)
