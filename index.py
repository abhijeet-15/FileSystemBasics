from pathlib import Path

# file_name = input("enter the file name to copy from: ")

# if ".env" in file_name.lower():
#     constent = input("allow reading an environment file. Y/N: ")
#     if constent.lower() == "y":
#         with open(file_name, "r") as rf:
#             with open(".example.env", "a") as wf:
#                 for line in rf:
#                     wf.write(line)
#     else:
#         raise PermissionError("Not allowed")

# else:
#     print("exiting")


# BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

# new_file = ""
# for p in Path().iterdir():
#     print(f"{p.name} : {p.stem} : {p.suffix}")
    
#     if p.stem == "demo":
#         new_file = Path(p.stem) / "new_file.py"
#         print(type(new_file))

# path = Path("text.txt").resolve()
# print(path.is_absolute())

# directory = Path.mkdir(self,parents=True, exist_ok=True)
# Path.iterdir()

# pattern = ".py"
# for p in Path.home().glob("*.py"):
#     print(p)

# for p in Path(Path.home() / "Desktop" / "dev" / "WeatherAssistant").glob("*.py"):
#     print(f"{p} : {p.stat().st_size}")'

# def _resolve_and_validate(self, target_path:str) -> Path:
#     resolved_path = 



# def edit_lines(self, file_path:str, start_line:int, end_line:int, new_content:str):
#     """Replaces a specific range of lines in a file."""
#     pass

class FileSystemTool:
    def __init__(self, base_directory="./"):
        self.base_directory = base_directory

    def write_file(self, file_name, content, mode='w'):
        """writes or appends to a file"""
        file_path = f"{self.base_directory}{file_name}"
        with open(file_path, mode, encoding="utf-8") as f:
            f.write(content)
        return f"successfully wrote to {file_name}"

    def read_file_generator(self, file_name):
        """A generator that yields one line at a time to prevent memory overload."""
        file_path = f"{self.base_directory}{file_name}"
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                yield line
    
    def copy_large_file(self, source_file_name, target_file_name):
        """Uses the generator to read and write line by line"""
        target_path = f"+{self.base_directory}{target_file_name}"
        with open(target_file_name, "w", encoding="utf-8") as target_file:
            for line in self.read_file_generator(source_file_name):
                target_file.write(line)
        
        return f"copied {source_file_name} to {target_file_name} line-by-line"

    

fs_tool = FileSystemTool()
result = fs_tool.copy_large_file("testfile.txt", "processed_data.txt")
print(result)
