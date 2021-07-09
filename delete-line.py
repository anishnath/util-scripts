import sys
import os

def delete_lines(original_file, line_numbers):
    is_skipped = False
    print(type(line_numbers))
    counter = 0
    print(type(counter))
    dummy_file = original_file + '.bak'
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        for line in read_obj:
            if counter not in line_numbers:
                write_obj.write(line)
            else:
                is_skipped = True
            counter += 1

    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)


user_input = input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
linerange=[0,1,2]
delete_lines(user_input,linerange)

