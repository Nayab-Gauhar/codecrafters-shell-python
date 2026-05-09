import sys


def main():
    while True:
        sys.stdout.write("$ ")
        commmand=input("")
        if commmand == "exit":
            break
        elif commmand.startswith("echo "):
            print(commmand[5:])
        else:
            print(f'{commmand}: command not found')
if __name__ == "__main__":
    main()
