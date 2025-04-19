def add_line_to_file_1(file, previous_line, new_line):
    with open(file, "r") as in_file:
        buf = in_file.readlines()
        if new_line in buf:
            print("Line already exists!")
            return 0
    with open(file, "w") as out_file:
        for line in buf:
            if line == previous_line:
                line = line + new_line
            out_file.write(line)

def find_append_to_file(file, find, insert):  # Dosesn't work
    with open(file, 'r+') as f:
        lines = f.read()

        index = repr(lines).find(find) - 1
        if index < 0 :
            raise ValueError("The text was not found in the file!")

        len_found = len(find) - 1
        old_line = lines[index + len_found:]

        file.seek(index)
        file.write(insert)
        file.write(old_line)

def add_line_to_file_2(file, previous_line, new_line):  #Only prints lines
    for line in open(file).readlines():
        print(line, end="")
        if line.startswith(previous_line):
            print(new_line)

file = "file_add_line.txt"
previous_line = "include below\n"
new_line = "included text\n"
add_line_to_file_1(file, previous_line, new_line)