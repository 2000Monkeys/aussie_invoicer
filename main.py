




def main():
    template_file           = str
    changeable_lines_amount = int
    list_of_lines           = []
    not_quit                = True

    while not_quit:
        initial_decider = input("type\n1 to open setup mode \n2 to invoice a client \n3 to reset template \n")
        if int(initial_decider) == 1:
            sufix = "#"
            template_file = open_and_read(int(initial_decider))
            changeable_lines_amount = get_varible_line_amount(template_file, sufix)
            get_edited_lines_names  = get_varible_lines(template_file, sufix)
            for i in range(changeable_lines_amount):
                message = get_edited_lines_names[i].strip() + ": "
                list_of_lines.append(input(message))


            template_file = change_template_lines(template_file, list_of_lines, sufix)

            create_active_template(template_file)

            not_quit = False

        elif int(initial_decider) == 2:
            sufix = "!"
            template_file = open_and_read(int(initial_decider))
            changeable_lines_amount = get_varible_line_amount(template_file, sufix)
            get_edited_lines_names  = get_varible_lines(template_file, sufix)
            for i in range(changeable_lines_amount):
                message = get_edited_lines_names[i].strip() + ": "
                list_of_lines.append(input(message))


            template_file = change_template_lines(template_file, list_of_lines, sufix)

            create_output_html(template_file)
            not_quit = False

        elif int(initial_decider) == 3:
            with open("template.txt", "r") as src:
                content = src.read()
            with open("active_template.txt", "w") as dst:
                dst.write(content)
            create_output_html(content)
            not_quit = False

        else:
            print("try again")




def open_and_read(type):
    if type == 1:
        with open("template.txt", "r") as file:
            return file.readlines()
    if type == 2:
        with open("active_template.txt", "r") as file:
            return file.readlines()

def get_varible_line_amount(file, sufix):
    x = 0
    for line in file:
        if sufix in line:
            #print(line)
            x += 1
    return x

def get_varible_lines(file, sufix):
    x = []
    for line in file:
        if sufix in line:
            x.append(line)
    return x

def change_template_lines(template_file, message, sufix):
    x = 0
    ret_file = [""]

    for line in template_file:

        if sufix in line:
            print(line, x)
            ret_file.append(str(message[x]))
            x += 1
        else:
            ret_file.append(line)

    return(ret_file)

def create_output_html(updated_file):
    with open("output.html", 'w') as file:
        file.writelines(updated_file)

def create_active_template(updated_file):
    with open("active_template.txt", 'w') as file:
        file.writelines(updated_file)


if __name__ == "__main__":
    main()
