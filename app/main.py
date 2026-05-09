import sys


def main():
    while True:
        builtin=['echo','exit','type']
        sys.stdout.write("$ ")
        commmand=input("")
        if commmand == "exit":
            break
        elif commmand.startswith("echo "):
            print(commmand[5:])
        elif commmand[:4] =='type':
            if commmand[5:] in builtin:
                print(f'{commmand[5:]} is a shell builtin')
            else:
                print(f'{commmand[5:]}: not found')
        else:
            print(f'{commmand}: command not found')
        
if __name__ == "__main__":
    main()
