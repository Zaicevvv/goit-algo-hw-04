from pathlib import Path

def get_cats_info(path):
    keys = ['id', 'name', 'age']
    result = []

    try:
        with open(path, encoding='utf-8') as fh:
            for element in fh.readlines():
                pet_data = element.strip().split(',')
                pet_dict = {}

                for i in range(3):
                    pet_dict.update({keys[i]: pet_data[i]})
                
                result.append(pet_dict)
                
            return result
    except:
        print('Something went wrong!')

current_dir = Path(__file__).parent
print(get_cats_info(current_dir / './data.txt'))