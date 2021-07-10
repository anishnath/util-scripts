import sys
import os

def print_or_delete_lines(original_file, line_numbers,action):
    is_skipped = False
    counter = 0
    dummy_file = original_file + '.bak'
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        for line in read_obj:
            if counter not in line_numbers:
                if action == "print":
                    print(line)
                else:
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
print_or_delete_lines(user_input,linerange,"print")
linerange=[1,2]
print_or_delete_lines(user_input,linerange,"delete")
print_or_delete_lines(user_input,linerange,"print")

