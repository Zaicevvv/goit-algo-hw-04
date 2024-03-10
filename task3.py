from colorama import Fore, Back, Style
import sys
from pathlib import Path

def open_dir(path):
    try:
        for dir in path.iterdir():
            if dir == Path('.git') or dir == Path('.venv'):
                continue
            elif dir.is_file():
                print(Style.RESET_ALL, Fore.BLUE, "   " if dir.parent != Path('.') else '', end='')
                print('📃', end=' ')
                print(f' {dir.name}' if dir.parent != Path('.') else f' {dir}')
            else:
                print('  📂', end='')
                print(Style.RESET_ALL, Fore.GREEN, dir)
                open_dir(dir)
    except:
        print(Fore.RED + 'Something went wrong')

if len(sys.argv) > 1:
    try:
        directory = Path(sys.argv[1])
        open_dir(directory)
    except:
        print(Fore.RED + 'Something went wrong')

#python task3.py ./