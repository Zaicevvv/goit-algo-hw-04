from pathlib import Path

def total_salary(path):
    try:
        with open(path, encoding='utf-8') as fh:
            file = [int(el.strip().split(',')[1]) for el in fh.readlines()]
            return sum(file), int(sum(file) / len(file))
    except FileNotFoundError:
        print('File not found!')

current_dir = Path(__file__).parent
print(total_salary(current_dir / './data.txt'))