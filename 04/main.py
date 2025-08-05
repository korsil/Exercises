from io import TextIOWrapper
import os

SAFE_DIR = os.path.abspath(os.path.normpath('/safedir'))

def is_safe_path(path: str) -> bool:
    # https://stackoverflow.com/a/45188896
    print(path)
    return os.path.commonpath((os.path.realpath(path), SAFE_DIR)) == SAFE_DIR 

def sanitize_path(path: str) -> str:
    path = os.path.normpath(path)

    index = path.find(SAFE_DIR)

    if(index != 0):
        path = os.path.join(SAFE_DIR, path)

    path = os.path.normpath(path)
    return path


def get_file(path: str)-> TextIOWrapper :
    sanitized_input = sanitize_path(path)
    if(not is_safe_path(sanitized_input)):
        raise Exception("Invalid path")
    if(not os.path.exists(sanitized_input)):
        raise Exception("File not found")
    return open(sanitized_input, 'r')


def main():
    print("Hello from 04!")
    print(get_file(input("File path: ")))



if __name__ == "__main__":
    main()
