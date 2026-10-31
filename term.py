import subprocess
import shlex

# with open("output.txt", "w") as f:
#     p = subprocess.run("ls -la", shell=True, stdout=f, text=True)

# p = subprocess.run("grep 'Fourth line' text.txt", shell=True, capture_output=True)
# pass print(p.stdout.decode())

# p1 = subprocess.Popen(["ls", "-la"], stdout=subprocess.PIPE, text=True)
# p2 = subprocess.run(["grep", ".txt"], stdin=p1.stdout, capture_output=True, text=True)
# p1.stdout.close()

# print(p2.stdout)

class TerminalCommandTool:
    def __init__(self, timeout=10):
        self.timeout = timeout
    
    def execute_terminal_command(self, command:str) -> str:
        
        forbidden_commands = ["rm", "sudo", "reboot", "nano"]
        parsed_command = shlex.split(command)
        if not parsed_command:
            return f"error: no command found"
        
        if parsed_command[0] in forbidden_commands:
            return f"error: not allowed to run the forbidden command"
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text= True,
                timeout=self.timeout
            )

            output = result.stdout
            if result.stderr:
                output += f"\n[Errors/Warnings]:\n{result.stderr}"
            
            return output.strip() if output else "command executed successfully with no output"
        
        except subprocess.TimeoutExpired:
            return f"error: command timedout after {self.timeout} seconds. Infinite loops or interactice prompts are blocked"

        except Exception as e:
            return f"System Error: {str(e)}"


t = TerminalCommandTool()
print(t.execute_terminal_command("ls -la"))
print(t.execute_terminal_command("echo 'Hello Agent'"))
print(t.execute_terminal_command("mkdir dummy_folder"))
