import sys


def main():
    while True:
        builtin=['echo','exit','type']
        sys.stdout.write("$ ")
        commmand=input("")
        if commmand[:4] in builtin:
            print(f'{commmand[5:]} is a shell builtin')
        if commmand == "exit":
            break
        elif commmand.startswith("echo "):
            print(commmand[5:])
        else:
            print(f'{commmand}: command not found')
        
if __name__ == "__main__":
    main()
