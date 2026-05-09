import sys


def main():
    while True:
        sys.stdout.write("$ ")
        commmand=input("")
        print(f'{commmand} : command not found')

if __name__ == "__main__":
    main()
