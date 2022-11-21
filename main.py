def number_of_line(*files):
    a = []
    text_f = []
    for file in files:
        with open(file, encoding='utf-8') as file_obj:
            text_f = file.obj.readlines()
            dline = len(text_f)
            name_file = file
            a.append([dline, name_file, [text_f]])
    return a.sort()
    print(a)
number_line = number_of_line('text1.txt', 'text2.txt', 'text3.txt')