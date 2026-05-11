import sys
import os
import shlex
import subprocess
import readline

def main():
    cmd_hist=['echo','exit']
    builtin=['echo','exit','type','pwd']
    def executable(command):
        for directories in os.environ['PATH'].split(os.pathsep):
            full_path=os.path.join(directories, command)
            if os.path.isfile(full_path) and os.access(full_path,os.X_OK):
                return full_path
        return None
    # # def paths(text):
    # #     try:
    # #         if cmd.startswith(text):
    # #             New_path=os.environ('PATH').split(os.pathsep)
    # #             for i in New_path:
    # #                 os.listdir(i)
                    
    #     except:
    #         return FileNotFoundError
    def completer(text,state):
        matches=[]
        # for builtiin functions
        for usr_input in cmd_hist:
            if usr_input.startswith(text):
                matches.append(usr_input+" ")
                # print(matches)
        #now for the directories matches
        for directory in os.environ['PATH'].split(os.pathsep):
            try:
                files=os.listdir(directory)
                for file in files:
                    if file.startswith(text):
                         full_path=executable(file)
                         if full_path:
                            matches.append(file+" ")
                         
            except FileNotFoundError:
                continue
            
        if len(matches) ==0 and state==0:
            sys.stdout.write("\x07")
            sys.stdout.flush()
        if state<len(matches):
            return matches[state]
        return None
    readline.set_completer(completer)
    readline.parse_and_bind('tab: complete')
    

    while True:
        # sys.stdout.write("$ ")
        # sys.stdout.flush()
        command=input("$ ")
        if not command:
            continue
        cmd=shlex.split(command)
        if cmd[0] == "exit":
            sys.exit()

            pass
        elif '>' in cmd or '1>' in cmd:
            if '>' in cmd:
                red_index=cmd.index('>')
            elif '1>' in cmd:
                red_index=cmd.index('1>')
            with open(cmd[-1],'w') as f:
                subprocess.run(cmd[:red_index],stdout=f)
        elif '2>' in cmd:
            if '2>' in cmd:
                red_index=cmd.index('2>')
            with open(cmd[-1],'w') as f:
                subprocess.run(cmd[:red_index],stderr=f)
        elif '>>' in cmd or '1>>' in cmd:
            if '>>' in cmd:
                red_index=cmd.index('>>')
            elif '1>>' in cmd:
                red_index=cmd.index('1>>')
            with open(cmd[-1],'a') as f:
                subprocess.run(cmd[:red_index],stdout=f)
        elif '2>>' in cmd:
            red_index=cmd.index('2>>')
            with open(cmd[-1],'a') as f:
                subprocess.run(cmd[:red_index],stderr=f)
        elif command.startswith("echo "):
            print(" ".join(cmd[1:]))
        elif cmd[0]=='pwd':
            print(os.getcwd())
        elif cmd[0]=='cd':
            if len(cmd)==1:
                os.chdir(os.getenv('HOME'))
            elif cmd[1]=='~':
                os.chdir(os.getenv('HOME'))
            else:
                if os.path.exists(cmd[1]):
                    os.chdir(cmd[1])
                else:
                    print(f'cd: {cmd[1]}: No such file or directory')
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
            new_path=executable(cmd[0])
            if new_path:
                subprocess.run(cmd)
            else:
                print(f'{cmd[0]}: command not found')
        
if __name__ == "__main__":
    main()
