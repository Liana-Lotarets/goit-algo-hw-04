from pathlib import Path
# Take color theme from "colorama"
from log import *

# Define a function that accepts a absolute path to a directory.
def structure_of_path_to_directory(absolute_path_to_directory: Path) -> str:
    if absolute_path_to_directory.exists():
        # This is a recursive function. 
        # It accepts the name of a directory, list of items of the one and a required space.
        # The space is equal to empty string by default.
        def structure_of_directory(name_dir: str, list_items: list, space = ''):
            # Write color name of the directory.
            result = f'{log_directory(name_dir)}:\n'
            # Define arrows to items of the directory.
            arrow = log_arrow('|' + '-'*len(name_dir) + '>')
            for item in list_items:
                # An item is a directory.
                if item.is_dir():
                    # Save the name of directory as "key" and the list of items as "value".
                    key, value = item.name, item.iterdir()
                    # Write an arrow taking into account the space.
                    result += space + arrow
                    # Create a new variable for "space" in order to pass to the recursive function
                    # and in order not to change the variable "space".
                    copy_space = space
                    copy_space += log_arrow('|') + ' '*len(name_dir)
                    result += structure_of_directory(key,value,copy_space)
                # An item is a file.
                else:
                    # Write an arrow taking into account the space and the name of the file.
                    result += space + arrow + f'{log_file(item.name)}\n'
            return result
        result = structure_of_directory(absolute_path_to_directory.name, 
                                        absolute_path_to_directory.iterdir())
        # Return ready structure without last "\n".
        return result[:-1]
    else:
        print('The path is not found.')
        return ''

# Example
my_path = Path('E:/Repository/goit-algo-hw-04/Task_3/Test_papk')
print(structure_of_path_to_directory(my_path))