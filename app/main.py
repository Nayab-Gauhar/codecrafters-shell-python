import sys
import os

def main():
    def executable(command):
        for directories in os.environ['PATH'].split(os.pathsep):
            full_path=os.path.join(directories, command)
            if os.path.isfile(full_path) and os.access(full_path,os.X_OK):
                return full_path
        return None

    builtin=['echo','exit','type']
    while True:
        sys.stdout.write("$ ")
        command=input("")
        if command == "exit":
            sys.exit()
        elif command.startswith("echo "):
            print(command[5:])
        elif command.startswith("type "):
            if command[5:] in builtin:
                print(f'{command[5:]} is a shell builtin')
            else:
                path=executable(command[5:])
                if path:
                    print(f'{command[5:]} is {path}')
                else:
                    print(f'{command[5:]}: not found') 

        else:
            print(f'{command}: command not found')
        
if __name__ == "__main__":
    main()
