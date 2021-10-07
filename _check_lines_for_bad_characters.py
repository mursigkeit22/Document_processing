import random


def count_numbers(value):
    count = 0
    for character in value:
        if character.isdigit():
            count += 1
    return count


def is_english(line):
    try:
        line.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


# собираем все строки в список
with open(r'work_docs\src.txt', "r", encoding="utf-8") as f:
    lines = f.readlines()

print(len(lines))

# удаляем всё из файла с будущими подходящими строками, если в нем что-то было
with open(r'work_docs\new.txt', "w", encoding="utf-8") as new_ff:
    pass

# создаем список с номерами подходящих строк и файл с самими строками (для удобства просмотра)
number_list = []
with open(r'work_docs\new.txt', "a", encoding="utf-8") as new_f:
    for number, line in enumerate(lines, start=1):
        split_line = line.split()
        if len(split_line) > 5:  # убираем строки, где слов меньше 6
            if not is_english(line):  # убираем строки, где есть non-ascii characters
                continue
            if "<" in line:
                continue
            count = count_numbers(line)
            if count < 7:  # убираем строки, где цифр больше 6
                number_list.append(number)
                new_f.write(line)

print(len(number_list))


# руками добрала нехватившие строки
hand_number_list = [73, 203, 237, 277, 384, 447, 508, 611, 625, 631, 632, 652, 663, 664, 771, 808, 828, 845, 921, 1132,
                    1416, ]

number_list = number_list + hand_number_list
print(len(set(number_list)))

# перемешиваем
shuffled_list = random.sample(number_list, 750)
print(len(shuffled_list))
print(shuffled_list)

# записываем номера строк в файл
with open("work_docs/done.SED", "w") as done_file:
    for el in shuffled_list:
        temp = str(el) + "p" + "\n"
        done_file.write(temp)

#  [73, 203, 237, 277, 384,  447,  508, 611, 625, 631,  632, 652, 663, 664, 771,  808, 828, 845, 921, 1132,
#  1140, 1143, 1158, 1237, 1244,   1245, 1254,1255, 1271, 1273,  1416, ]
