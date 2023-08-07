import sys

def main():
    print(f"sys.argv prints all the arguments at the cmd including fule name")
    print(f"len(sys.argv)prints the total number of arg in cmd{len(sys.argv)}")

    for arg in sys.args:
        print(arg)
if __name__=="__main__":
    main()
