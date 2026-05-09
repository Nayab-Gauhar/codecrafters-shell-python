import sys
import os
import shlex
import subprocess

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
        if not command:
            continue
        cmd=shlex.split(command)
        print()
        if cmd[0] == "exit":
            sys.exit()
        elif command.startswith("echo "):
            print("".join(cmd[1:]))
        elif command.startswith("type "):
            if cmd[1] in builtin:
                print(f'{cmd[1]} is a shell builtin')
            else:
                path=executable(cmd[1])
                if path:
                    print(f'{cmd[1]} is {path}')
                else:
                    print(f'{cmd[1]}: not found') 

        else:
            print(f'{command}: command not found')
        
if __name__ == "__main__":
    main()
