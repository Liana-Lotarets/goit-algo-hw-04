# The begin
def get_cats_info(path: str) -> list[dict]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            # Create a list of information about every cats.
            lines = [line.strip() for line in file.readlines()]
            # Create a list of dictionaries of information about cats and return the one.
            list_of_dict_of_cats = []
            for line in lines:
                info = line.split(',')
                list_of_dict_of_cats.append({'id': info[0], 'name': info[1], 'age': info[2]})
                del(info)
            return list_of_dict_of_cats
    except Exception as excpt:
        print(f'Sorry, but {excpt}.')
        return [{}]
# The end

cats_info = get_cats_info("Task_2/cats.txt")
print(cats_info)