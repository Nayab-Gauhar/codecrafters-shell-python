import sys


def main():
    while True:
        sys.stdout.write("$ ")
        commmand=input("")
        print(f'{commmand}: command not found')
        if commmand == "exit":
            break
if __name__ == "__main__":
    main()
